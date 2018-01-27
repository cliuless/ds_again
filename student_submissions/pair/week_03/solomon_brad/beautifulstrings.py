"""CodeEval Beautiful Strings challenge.

https://www.codeeval.com/browse/83/
"""

from collections import Counter
from operator import itemgetter
import re

SCORES = range(26, 0, -1)
NONALPHA = re.compile('[^a-z]')


def beautify_string(s):
    letters = NONALPHA.sub('', s.lower())
    return sum(i * j for i, j in
               zip(SCORES, map(itemgetter(1),
                               Counter(letters).most_common())))


def rank_file(path):
    lines = tuple(open(path, 'r'))
    for line in lines:
        print(beautify_string(line))


if __name__ == '__main__':
    rank_file('input/strings.txt')
