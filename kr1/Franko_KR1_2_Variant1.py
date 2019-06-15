import math
#ax6 + bx3 + c = 0
a = float(input('Введите коэффициент a '))
b = float(input('Введите коэффициент b '))
c = float(input('Введите коэффициент c '))
dskr = b**2-4*a*c
if a !=0:
    if dskr <0:
        print('Решений нет')
    elif dskr == 0:
        print('Бесконечно решений')
    else:
        print('Два решения')

else:
    print('Одно решение')








































''' t1 = (-b + math.sqrt(dskr))/2*a
    t2 = (-b - math.sqrt(dskr))/2*a
    x1 = t1**(1/3)
    x2 = t2**(1/3)'''
