#import random
n = input('Введите число лицеистов ')
integer = int(n)
#n = str(random.randint(0, 1001))
lastdigit = int(n[-1])
if len(n)!=1:
    twolastdigits = int(n[-2]+str(lastdigit))
if lastdigit == 1 and integer!=11:
    print(n, 'лицеист')
elif lastdigit<=9 and lastdigit>=5:
    print(n, 'лицеистов')
elif len(n)>1 and twolastdigits<=19 and twolastdigits>=11:
    print(n, 'лицеистов')
elif lastdigit<=4 and lastdigit>=2:
    print(n, 'лицеиста')
elif integer == 0:
    print('Лицеистов нет')
else:
    print(n, 'лицеистов')

#Программа не ограничивается числом от 0 до 1000. Она корректно работает и с большими числами
