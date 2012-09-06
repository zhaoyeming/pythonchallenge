"""Challenge 12 at http://www.pythonchallenge.com/pc/return/evil.html"""

import imghdr

if __name__ == '__main__':
    with open('evil2.gfx', 'r') as f:
        data = f.read()

        # Split file into 5 files.
        # And because the 4th file is malformed, we don't try to display it in
        # the program but write all of them to disk and open them externally.
        for start in range(5):
            pic = data[start::5]
            suffix = imghdr.what(None, pic)
            with open(str(start) + '.' + suffix, 'w') as pic_file:
                pic_file.write(pic)
