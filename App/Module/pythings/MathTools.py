def test():
    print('Test Complete. Pythings MathTools working.')
    return 'MathTools Working'

def fib(num, length = 'one'):
    num1 = 0
    num2 = 1
    numlist = []
    looper = 0
    if num <= 0:
        raise ValueError('"' + num+'" is not a valid arguement for num. Valid values must be above 0.')
    while looper < int(num):
        looper=looper+1
        numlist.append(num1)
        numlist.append(num2)
        num1 = num1 + num2
        num2 = num2 + num1
    if length == 'one':
        return numlist[int(num)]
    elif length == 'all':
        return numlist
    else:
        raise ValueError('"'+length+'" is not a valid argument for length. Valid arguements are "one" and "all"')
