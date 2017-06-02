#!/usr/bin/env python3

import os

import jinja2

import parser

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATES_DIR = os.path.join(ROOT, 'templates')
BUILD_DIR = os.path.join(ROOT, 'build')

JINJA = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIR))
JINJA.filters.update({
    'issection': lambda obj: isinstance(obj, parser.Section),
    'issubsection': lambda obj: isinstance(obj, parser.SubSection),
    'isquestion': lambda obj: isinstance(obj, parser.Question),
})
TEMPLATE = JINJA.get_template('index.html')

def render(objects):
    # TODO: TOC, intro, and instructions
    return TEMPLATE.render(objects=objects)

def main():
    objects = parser.parse(parser.gettext())
    with open(os.path.join(BUILD_DIR, 'index.html'), 'w') as fp:
        fp.write(render(objects))

if __name__ == '__main__':
    main()
