"""Challenge 3 at http://www.pythonchallenge.com/pc/def/equality.html"""

if __name__ == '__main__':
    with open('challenge_3.dat', 'r') as f:
        # Add one lower letter to the string at each end, so that our 9-char
        # window will work at the boundary.
        data = 'a' + f.read().replace('\n', '') + 'a'

        letters_iter = (data[i:i+9] for i in range(len(data) - 9))
        print ''.join(
            [letters[4]
             for letters in letters_iter if (letters[0].islower() and
                                             letters[1:4].isupper() and
                                             letters[4].islower() and
                                             letters[5:8].isupper() and
                                             letters[8].islower())
             ]
        )
