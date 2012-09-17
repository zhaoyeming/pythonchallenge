"""Challenge 14 at http://www.pythonchallenge.com/pc/return/italy.html"""

from itertools import repeat, chain
import png


def next_deltas(row_delta, col_delta):
    next_deltas_mapping = {
        (0, 1):  (1, 0),
        (1, 0):  (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
        }
    current_deltas = (row_delta, col_delta)
    return next_deltas_mapping[current_deltas]


if __name__ == '__main__':
    _, _, p, _ = png.Reader('wire.png').read()
    pixels = iter(next(p))

    # We are going to draw a 100*100 pic
    pic = [[0]*100 for i in range(100)]

    row, col = 0, -1  # initially left to the first cell (top-left pixel)
    row_delta, col_delta = 0, 1  # initial direction points to right

    # Produce sequence 100, 99, 99, 98, 98, ... , 1, 1
    for seq in chain([100], *(repeat(i, 2) for i in xrange(99, 0, -1))):
        for _ in range(seq):
            row += row_delta
            col += col_delta
            R, G, B = next(pixels), next(pixels), next(pixels)
            pic[row][col] = [R, G, B]

        # Now it's time to turn right
        row_delta, col_delta = next_deltas(row_delta, col_delta)

    # Transform to the format the PyPNG accepts
    array = [list(chain(*row)) for row in pic]
    png.from_array(array, 'RGB').save('challenge_14.png')


    # There's a cat in challenge_14.png. Looking at
    # http://www.pythonchallenge.com/pc/return/cat.html, we know its name is
    # "uzi". http://www.pythonchallenge.com/pc/return/uzi.html is the answer.
