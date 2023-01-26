
a = 'gato'
b = 'O gato subiu no telhado'
c = 'telhado'

print(a > b)
print(c == b[16:])
print(a == b[2:5])
print(a == b[2:6])
print(a == b)
print(a > c)
print(a != c)
print(c == b[15:])

def fazAlgo(string):
    pos = len(string)-1
    string = string.upper()
    while pos >= 0:
        print(string[pos],end = "")
        pos = pos - 1

fazAlgo("paralelepipedo")

def fazAlgo(string):
    pos = 0
    string1 = ""
    string = string.lower()
    stringMa = string.upper()
    while pos < len(string):
        if pos % 2 == 0:
            string1 = string1 + stringMa[pos]
        else:
            string1 = string1 + string[pos]
        pos = pos + 1
    return string1

print(fazAlgo("paralelepipedo"))

x = 10
x += 10
x /= 2
x //= 3
x %= 2
x *= 9
print(x)

def calculo(x, y = 10, z = 5):
    return x + y * z;
print(calculo(2,12,10))


def horario_em_segundos(h, m, s):
    assert h >= 0 and m >= 0 and s >= 0
    return h * 3600 + m * 60 + s


print(horario_em_segundos(-1, 20, 30))
#comando assert é acessão