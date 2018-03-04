#!/usr/bin/env python
from __future__ import print_function

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    word, count = line.split('\t')
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            print('{}\t{}'.format(current_word, current_count))
        current_word = word
        current_count = count

if current_word == word:
    print('%s\t%i' % (current_word, current_count))

