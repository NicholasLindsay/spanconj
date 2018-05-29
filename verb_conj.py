#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse

# a naive Spanish verb conjugater

# conjugation tables
ar_conjugations = {
    'fp'  : 'o',
    'sp'  : 'as',
    'tp'  : 'a',
    'fpp' : 'amos',
    'spp' : 'áis',
    'tpp' : 'an',
    }

er_conjugations = {
    'fp'  : 'o',
    'sp'  : 'es',
    'tp'  : 'e',
    'fpp' : 'emos',
    'spp' : 'éis',
    'tpp' : 'en',
    }

ir_conjugations = {
    'fp'  : 'o',
    'sp'  : 'es',
    'tp'  : 'e',
    'fpp' : 'imos',
    'spp' : 'ís',
    'tpp' : 'en',
    }


# stem: returns the stem (removes the infinitive ending)
def stem(infinitive):
    if infinitive[-2:] == 'ar':
      return infinitive[:-2]
    elif infinitive[-2:] == 'er':
      return infinitive[:-2]
    elif infinitive[-2:] == 'ir':
      return infinitive[:-2]
    else:
      print('Unknown verb form\n')
      quit()

# verb ending type (ar, er, ir)
def ending_type(infinitive):
    ending = infinitive[-2:]
    if ending != 'ar' and ending != 'er' and ending != 'ir':
        print('Unknown verb form\n')
        quit()
    return ending

# conjugate: conjugates an infinitive with a specific subject type
def conjugate(infinitive, subject):
    the_stem = stem(infinitive)
    ending = ''

    if ending_type(infinitive) == 'ar':
        ending = ar_conjugations[subject]
    elif ending_type(infinitive) == 'er':
        ending = er_conjugations[subject]
    elif ending_type(infinitive) == 'ir':
        ending = ir_conjugations[subject]

    return the_stem + ending;

# sets up argument parser
def setup_argparse():
    parser = argparse.ArgumentParser(description='Conjugate Spanish verbs')
    parser.add_argument('-t', help='verb tenses', nargs='+', dest='tenses', default=[])
    parser.add_argument('-s', help='verb subject', nargs='+', dest='subjects', default=[])
    parser.add_argument('infinitive')
    return parser

def main(args=None):
    """ Main function """
    parser = setup_argparse()
    args = parser.parse_args()

    if len(args.tenses) == 0:
        args.tenses = []
    if len(args.subjects) == 0:
        args.subjects = ['fp','sp','tp','fpp','spp','tpp']
        
    for subject in args.subjects:
        print(conjugate(args.infinitive, subject))

if __name__ == "__main__":
    main()
