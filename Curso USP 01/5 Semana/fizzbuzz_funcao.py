def fizzbuzz(x):

    if (x % 3 == 0) and (x % 5 != 0):
        y = 'Fizz'
        return y
    elif(x % 5 == 0) and (x % 3 != 0):
        y = 'Buzz'
        return y
    elif(x % 5 == 0) and (x % 3 == 0):
        y = 'FizzBuzz'
        return y
    else:
        y = x
        return y

def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(4) == 4



#print(test_fizzbuzz())
print(fizzbuzz(28))