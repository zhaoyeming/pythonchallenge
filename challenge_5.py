"""Challenge 5 at http://www.pythonchallenge.com/pc/def/peak.html"""

import pickle
import sys

if __name__ == '__main__':
    with open('challenge_5.dat', 'r') as f:
        data = pickle.load(f)
        for line in data:
            for c, n in line:
                sys.stdout.write(c * n)
            print
