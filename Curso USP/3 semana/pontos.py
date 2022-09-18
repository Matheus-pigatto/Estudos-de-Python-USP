import math
x1 = float(input('Digite a cordenada X do primeiro ponto: '))
y1 = float(input('Digite a cordenada Y do primeiro ponto: '))
x2 = float(input('Digite a cordenada X do segundo ponto: '))
y2 = float(input('Digite a cordenada Y do segundo ponto: '))

dist = math.sqrt((x1-x2)**2+(y1-y2)**2)

print(f'{dist:.4}')
if dist > 10:
    print('longe')
else:
    print('perto')