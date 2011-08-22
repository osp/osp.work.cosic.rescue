#!/usr/bin/env python

'''
Basic usage:

    >>> text = "Antoon Bosselears is a super guy"
    >>> make_oblique(text)
    u'result'

    >>> text = """
    ... COSIC
    ... K. U. Leuven 
    ... Kasteelpark Atenberg 10 
    ... B-3001 Heverlee
    ... (Belgium)
    ... """
    >>> make_oblique(text)
    u'result'

    >>> text = """
    ... Je t'aime
    ... ma bichette
    ... """
    >>> make_oblique(text)
    u'result'
'''


def make_oblique(text):
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
    

    #import pdb; pdb.set_trace()
    for i in xrange(len(words[0])):
        current = "   ".join(word[i] for word in words)
        output += current.rjust(i + len(current), " ")
        output += "\n"

    print(output)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    text = """
    COSIC - K. U. Leuven 
    Kasteelpark Atenberg 10 
    B-3001 Heverlee (Belgium)
    """
    make_oblique(text)

