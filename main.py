#! /usr/bin/env python3

import sys
from spellchecker import SpellChecker

spell = SpellChecker(language='es')

def main():
    print(spell.candidates('test'))

if __name__ == '__main__':
    main();
