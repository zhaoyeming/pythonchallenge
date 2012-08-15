"""Challenge 5 at http://www.pythonchallenge.com/pc/def/peak.html"""

import pickle

if __name__ == '__main__':
    with open('challenge_5.dat', 'r') as f:
        data = pickle.load(f)
        for line in data:
            print ''.join([c * n for c, n in line])
