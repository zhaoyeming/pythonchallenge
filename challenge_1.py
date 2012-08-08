"""Challenge 1 at http://www.pythonchallenge.com/pc/def/map.html"""

import string

hint = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
url = "map"

if __name__ == '__main__':
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alphabet[2:] + alphabet[:2]
    table = string.maketrans(alphabet, shifted)
    print hint.translate(table)
    print url.translate(table)
