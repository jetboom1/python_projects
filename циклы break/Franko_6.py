import math
a = int(input('Введите число'))
for i in range(2,int(math.sqrt(a))+1):
    if a%i==0:
        print('Это НЕ простое число')
        break
else:
    print('Это простое число')
