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
import numpy as np


def make_oblique_4(text, line_spacing=1, slant=1, letter_spacing=1, reverse=False):
    lines = text.splitlines()  # Splits the text at newlines
    max_len = max([len(x) for x in lines])
    lines = [x.ljust(max_len) for x in lines]

    if reverse:
        lines.reverse()

    # Computes the size of or canvas
    n_row = (len(max(lines)) + (len(lines) * line_spacing)) * slant
    n_col = len(max(lines)) + (len(max(lines)) * letter_spacing)

    # Creates the canvas
    canvas = np.zeros((n_row, n_col), dtype='S1')
    canvas[...] = ' '  # ye mighty FORTRAN, we beseech thee

    for i, line in enumerate(lines):
        letters_x = np.multiply(np.arange(len(line)), letter_spacing)
        letters_y = np.multiply(np.arange(len(line)), slant)
        canvas[letters_y + (i * line_spacing), letters_x] = list(line)

    canvas[:, -1] = '\n'
    if reverse:
        canvas = canvas[::-1]
    return canvas.tostring().rstrip()


def make_oblique_3(text):
    import numpy as np
    words = text.splitlines()
    n = max(4 * len(word) for word in words) + len(words)
    canvas = np.zeros((n, n), dtype='S1')
    canvas[...] = ' '  # ye mighty FORTRAN, we beseech thee

    for j, word in enumerate(words):
        i = np.arange(len(word))
        canvas[i + j * 4 , 2 * i] = list(word)

    canvas[:, -1] = '\n'
    return canvas.tostring().rstrip()


def make_oblique_2(text):
    words = text.splitlines()
    matrix = [[" " for i in xrange(len(words) + len(max(words)))] \
            for j in xrange(len(words) + len(max(words)))]
    for i, word in enumerate(words):
        for j, letter in enumerate(word):
            matrix[j + i][j] = letter
    matrix = map(lambda x: "".join(x), matrix)
    return "\n".join(matrix)


def make_oblique(text, separator="   ", invert=False):
    """docstring for make_oblique"""
    max_len = 0
    output = ""
    words = text.split("\n")

    if invert:
        inverted = []
        for word in words:
            w = list(word)
            w.reverse()
            w = "".join(w)
            inverted.append(w)
        words = inverted

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

    for i in xrange(max_len):
        current = separator.join(word[i] for word in words)
        if invert:
            output += current.rjust((max_len - i) + len(current), " ")
        else:
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
    parser.add_argument('-i', '--invert', default=False, action="store_true", help='Invert direction')

    args = parser.parse_args()

    if args.text is None:
        print(make_oblique(sys.stdin.read(), separator=args.separator, invert=args.invert))
    else:
        print(make_oblique(args.text, separator=args.separator))
