"""Challenge 13 at http://www.pythonchallenge.com/pc/return/disproportional.html"""

import xmlrpclib

if __name__ == '__main__':
    # The phonebook.php found in the source is a XML-RPC service.
    proxy = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/'
                                  'phonebook.php')

    # After trying 'call' and 'phone', we found it's the 'phone' method.
    # And last challenge #12, we know that Bert is evil.
    print proxy.phone('Bert')
