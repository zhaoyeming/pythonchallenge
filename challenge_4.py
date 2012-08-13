"""Challenge 4 at http://www.pythonchallenge.com/pc/def/linkedlist.php"""

import sys
import urllib2


URL_FMT = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'

if __name__ == '__main__':
    pointer = '12345'
    while True:
        url = URL_FMT.format(pointer)
        content = urllib2.urlopen(url).read()
        try:
            pointer = content.rsplit(' ', 1)[1]
        except IndexError:
            print content
            sys.exit(0)
