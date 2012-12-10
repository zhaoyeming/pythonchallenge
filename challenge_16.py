"""Challenge 16 at http://www.pythonchallenge.com/pc/return/mozart.html"""


import Image


if __name__ == '__main__':
    # By looking at the picture, we found that every row has a mark segment
    # with color palette number 195.
    # The hint in the web page says "let me get this straight", so we try
    # align the mark segments to a straight line.

    im = Image.open('mozart.gif')
    x, y = im.size
    data = list(iter(im.getdata()))
    new_data = []

    for j in range(y):
        start = j * x
        end = start + x
        row = data[start:end]
        mark = row.index(195)
        # shift row, making it start at the mark position
        new_row = row[mark:] + row[:mark]
        new_data += new_row

    im.putdata(new_data)
    im.show()

    # The picture now shows "romance". So the URL of next level is
    # http://www.pythonchallenge.com/pc/return/romance.html
