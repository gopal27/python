#!/usr/bin/python

import bisect
import sys

HAYSTACK = [0, 1, 4, 5, 5, 8, 9, 11, 12, 12, 13, 18, 23, 24, 30]
NEEDLE = [0, 2, 4, 6, 7, 10, 22, 39]



ROW_FMT = '{0:2d} @ {1:2d}          {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLE):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))




if __name__ == '__main__':
    
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

