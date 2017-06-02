#!/usr/bin/env python3

import collections
import os
import re

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(HERE)
TXT = os.path.join(ROOT, 'data/2014-2018 Tech Pool.processed.txt')

H2 = re.compile(r'^SUBELEMENT (?P<id>T\d) - (?P<title>.*)\n\n?')
H3 = re.compile(r'(?P<id>T\d[A-Z]) - (?P<title>.*)\n\n?')
QA = re.compile(r'(?P<id>T\d[A-Z]\d{2}) \((?P<answer>[A-D])\)(?P<ref>.*)\n'
                r'(?P<question>.*)\n'
                r'A\. (?P<A>.*)\n'
                r'B\. (?P<B>.*)\n'
                r'C\. (?P<C>.*)\n'
                r'D\. (?P<D>.*)\n'
                r'~~\n\n?')

Section = collections.namedtuple('Section', 'id title')
SubSection = collections.namedtuple('SubSection', 'id title')
Question = collections.namedtuple('Question', 'id ref question choices answer')
Choice = collections.namedtuple('Choice', 'id text')

def gettext():
    with open(TXT) as fp:
        return fp.read()

def parse(text):
    objects = []
    processed_chars = 0
    while text:
        m = H2.match(text)
        if m:
            objects.append(Section(m['id'], m['title']))
            processed_chars += len(m[0])
            text = text[len(m[0]):]
            continue
        m = H3.match(text)
        if m:
            objects.append(SubSection(m['id'], m['title']))
            processed_chars += len(m[0])
            text = text[len(m[0]):]
            continue
        m = QA.match(text)
        if m:
            choices = [Choice(choice, m[choice]) for choice in 'ABCD']
            objects.append(Question(m['id'], m['ref'].strip(), m['question'], choices, m['answer']))
            processed_chars += len(m[0])
            text = text[len(m[0]):]
            continue
        raise RuntimeError(f'Unrecognized (char {processed_chars}): {text[:50]}...')
    return objects
