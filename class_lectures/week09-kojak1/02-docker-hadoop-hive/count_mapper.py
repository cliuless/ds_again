#!/usr/bin/env python
from __future__ import print_function

import sys
from textblob import TextBlob

for line in sys.stdin:
    line = line.decode('utf-8')
    words = TextBlob(line).words
    for word in words:
        word = word.encode('utf-8')
        print("{}\t{}".format(word, 1))

