#!/usr/bin/env python3

import os

import jinja2

import parser

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATES_DIR = os.path.join(ROOT, 'templates')
SITE_ROOT = os.path.join(ROOT, 'site')

JINJA = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
JINJA.filters.update({
    'issection': lambda obj: isinstance(obj, parser.Section),
    'issubsection': lambda obj: isinstance(obj, parser.SubSection),
    'isquestion': lambda obj: isinstance(obj, parser.Question),
})
TEMPLATE = JINJA.get_template('index.html')

def gather_sections(objects):
    sections = []
    subsections = []
    section = None
    for obj in objects:
        if isinstance(obj, parser.Section):
            if section:
                sections.append((section, subsections))
                subsections = []
            section = obj
        elif isinstance(obj, parser.SubSection):
            subsections.append(obj)
    if section:
        sections.append((section, subsections))
    return sections

def render(objects):
    sections = gather_sections(objects)
    return TEMPLATE.render(objects=objects, sections=sections)

def main():
    objects = parser.parse(parser.gettext())
    with open(os.path.join(SITE_ROOT, 'index.html'), 'w') as fp:
        fp.write(render(objects))

if __name__ == '__main__':
    main()
