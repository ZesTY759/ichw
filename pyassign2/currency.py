"""currency.py: To convert one currency into another at an exchange rate.

__author__ = "Zhang Tianyu"
__pkuid__  = "1800011759"
__email__  = "1800011759@pku.edu.cn"
"""

def exchange(currency_from,currency_to,amount_from):
    """In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.
    When the currency type error or numerical error, remind the user 
    of the error cause.
    Parameter currency_from is a string: the currency on hand
    Parameter currency_to is a string: the currency to convert to
    Parameter amount_from is a string: amount of currency to convert
    Return is a float: amount of currency received in the given exchange.
    """
    import json
    from urllib.request import urlopen
    
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    dic = json.loads(jstr)
    
    suc1='{success}'.format(**dic)
    to1='{to}'.format(**dic)
    error1='{error}'.format(**dic)
    if suc1=='True':
        to2=to1.split(' ')
        re=float(to2[0])
        return re
    else:
        return error1
    
def test_amount_to():
    """verify that the data values are correct and 
    that the data types are correct (it should be a float)
    """
    assert(3.673162 == exchange('USD','AED',1)),'output error'
    assert(0.777993 == exchange('USD','IMP',1)),'output error'
    assert(0.070368024769545 == exchange('UAH','USD',2)),'output error'

def test_currency(): 
    """verify that the user input currency type is correct
    """
    assert('Source currency code is invalid.'==exchange('AAA','AED',1)),'validity verification error'
    
def test_amount_from():
    """verify that the values entered by the user are valid"""
    assert('Currency amount is invalid.'==exchange('USD','AED','a')),'validity verification error'

def testAll():
    """test all cases
    """
    test_amount_to()
    test_currency()
    test_amount_from()
    print("All tests passed")

def main():
    """main module
    """
    testAll()
    
if __name__ == '__main__':
    main()
