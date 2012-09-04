"""Challenge 11 at http://www.pythonchallenge.com/pc/return/5808.html"""

import Image


def is_odd(n):
    return n % 2 == 1


if __name__ == '__main__':
    im = Image.open('cave.jpg')

    odds = []
    evens = []

    x, y = im.size
    it = iter(im.getdata())

    for row in range(y):
        for col in range(x):
            point = it.next()
            if is_odd(row):
                if is_odd(col):
                    odds.append(point)
                else:
                    evens.append(point)
            else:
                if is_odd(col):
                    evens.append(point)
                else:
                    odds.append(point)

    image_odd = Image.new('RGB', (x / 2, y))
    image_odd.putdata(odds)
    image_odd.show()
