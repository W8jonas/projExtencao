oi = ('2' * 3).__len__()
print(oi)

if 20 > 3:
    print('maior')
else:
    print('menor')

i = 1

while i < 2:
    i += 1
    print('a')


def soma(a, b):
    return a+b


valor = soma(100, 200)
print(valor.__str__()*2)
