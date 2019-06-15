a = float(input('Введите a '))
b = float(input('Введите b '))
c = float(input('Введите c '))
d = float(input('Введите d '))
s = float(input('Введите s '))
t = float(input('Введите t '))
u = float(input('Введите u '))
check = (s*a+t*b+u)*(s*c+t*d+u)
if s==0 and t==0:
    print('s и t не может равнятся нулю одновременно')

else:
    if check>0:
        print('Точки принадлежат разным полуплоскостям')
    elif check<0:
        print('Точки лежат в одной полуплоскости')
