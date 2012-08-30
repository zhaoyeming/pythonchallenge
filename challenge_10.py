"""Challenge 10 at http://www.pythonchallenge.com/pc/return/bull.html"""

from itertools import groupby

a = ['1', '11', '21', '1211', '111221']
N = 30


def describe(numstr):
    for k, g in groupby(numstr):
        yield str(len(list(g)))
        yield str(k)


if __name__ == '__main__':
    while len(a) <= N:
        last_item = a[-1]
        next_item = ''.join(list(describe(last_item)))
        a.append(next_item)

    print len(a[N])
