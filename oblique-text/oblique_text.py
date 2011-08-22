#!/usr/bin/env python

'''
Basic usage:

    >>> text = """Super
    ... Cool"""
    >>> print(make_oblique(text))
    S   C
     u   o
      p   o
       e   l
        r    
    <BLANKLINE>
'''

import sys
from textwrap import dedent
import fileinput


def make_oblique(text, separator="   "):
    """docstring for make_oblique"""
    words = text.split("\n")
    max_len = 0
    output = ""

    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    for i, word in enumerate(words):
        for j in xrange(max_len - len(word)):
            words[i] += " "

    #for word in words:
        #for i, letter in enumerate(word):
            #output += letter.rjust(i + 1, " ")
            #output += "\n"

    #print(output)

    for i in xrange(len(words[0])):
        current = separator.join(word[i] for word in words)
        output += current.rjust(i + len(current), " ")
        output += "\n"

    return output


if __name__ == "__main__":
    #import doctest
    #doctest.testmod()

    import argparse

    parser = argparse.ArgumentParser(description='Makes a text oblique')
    parser.add_argument('-t', '--text', default=None, help='The text to process')
    parser.add_argument('-s', '--separator', default="   ", help='The character(s) to seperate words')

    args = parser.parse_args()

    if args.text is None:
        print(make_oblique(sys.stdin.read(), separator=args.separator))
    else:
        print(make_oblique(args.text, separator=args.separator))
