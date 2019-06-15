string = input('Введите число')
for i in string:
    if i.isdigit()==False and i != 'A' and i != 'B' and i != 'C' and i != 'D' and i != 'E' and i != 'F':
        print('Это число не может быть представлено в 16-ричной системе счисления')
        break
else:
    print('Число можно представить в 16-ричной системе счисления')

