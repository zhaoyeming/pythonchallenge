"""Challenge 6 at http://www.pythonchallenge.com/pc/def/channel.html"""

from zipfile import ZipFile, ZipInfo

if __name__ == '__main__':
    next_file = '90052.txt'
    comments = ''

    with ZipFile('channel.zip', 'r') as z:
        while True:
            try:
                f = z.open(next_file, 'r')
                comments += z.getinfo(next_file).comment
                content = f.read()
                next_file = content.rsplit(' ', 1)[1] + '.txt'
            except:
                print comments
                break
