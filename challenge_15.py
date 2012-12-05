"""Challenge 15 at http://www.pythonchallenge.com/pc/return/uzi.html"""

from datetime import date


def is_leap(year):
    try:
        date(year, 2, 29)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    # all years starts with 1 and ends with 6
    years = [int('1' + str(i) + '6') for i in range(100)]

    # those years that are leap years (because Feb has 29 days in calenday)
    years = [year for year in years if is_leap(year)]

    # those years that Jan 26. is Monday
    years = [year for year in years if date(year, 1, 26).weekday() == 0]

    # 2nd youngest in the years list
    year = years[-2]

    # "tomorrow" of marked date is Jan. 27
    print date(year, 1, 27)

    # 1756-01-27 is birthday of Mozart. The answer to this puzzle is
    # http://www.pythonchallenge.com/pc/return/mozart.html
