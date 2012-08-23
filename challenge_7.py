"""Challenge 7 at http://www.pythonchallenge.com/pc/def/oxygen.html"""

from itertools import takewhile, islice
import png

if __name__ == '__main__':
    _, height, pixels, _ = png.Reader('oxygen.png').read()
    rows = list(pixels)
    row_of_interest = rows[height / 2]

    # group by every 4 numbers. see recipes of itertools doc
    points = zip(*((iter(row_of_interest),) * 4))

    # points with R == G == B are what we want
    points_of_interest = takewhile(lambda x: x[0] == x[1] == x[2], points)

    # 7 pixels per same color
    sample_points = islice(points_of_interest, 0, None, 7)

    # get hint
    ascii_values = [p[0] for p in sample_points]
    hint = ''.join(map(chr, ascii_values))
    print hint

    # next step: interpret hint
    l = eval(hint[hint.find('['):])
    print ''.join(map(chr, l))
