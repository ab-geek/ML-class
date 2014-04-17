# -*- coding: utf-8 -*-

import re

text = ""
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

#print(sentences)

import re as re
 
def splitParagraphIntoSentences(paragraph):
    sentenceEnders = re.compile(r"""
       # Split sentences on whitespace between them.
       (?:               # Group for two positive lookbehinds.
         (?<=[" "। ])      # Either an end of sentence punct,
       | (?<=[| ]['"])  # or end of sentence punct and quote.
       )                 # End group of two positive lookbehinds.
      
       \s+               # Split on whitespace between sentences.
       """,
        re.IGNORECASE | re.VERBOSE)
    return sentenceEnders.split(paragraph)
 
if __name__ == '__main__':
    f = open("31_51262.txt", 'r')
    text = f.read()
    sentences = splitParagraphIntoSentences(text)
    longsentences = 0
    sentencecount = 0
    totalwords = 0
    for i in sentences:
        print i.strip()       #  a sentence
        lst1 = i.split(' ')
        print "sentence length",len(lst1)
        if len(lst1) > 20: longsentences += 1
        sentencecount += 1
        totalwords += len(lst1)
        print '------------------------------------------------------'
    print "Number of sentences =",sentencecount
    print "Number of words     =",totalwords
    print "Long sentences      =",longsentences
    print "Av sentence length  =",(totalwords+0.0)/sentencecount
