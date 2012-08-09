"""Challenge 2 at http://www.pythonchallenge.com/pc/def/ocr.html"""

if __name__ == '__main__':
    with open('challenge_2.dat', 'r') as f:
        print ''.join([c for c in f.read() if c.isalpha()])
