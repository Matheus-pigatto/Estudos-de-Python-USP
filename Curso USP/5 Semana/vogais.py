def vogal(x):
    if x in 'AaEeIiOoUu':
        return True
    else:
        return False

def test_vogal():
    assert vogal('a') == True
    assert vogal('B') == False
    assert vogal('d') == False
    assert vogal('i') == True

print(vogal('a'))
#print(test_vogal())