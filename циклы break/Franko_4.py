string = input('Введите число')
for i in string:
    if i.isdigit()==False:
        print('Это число не может быть представлено в системе счисления с основанием меньше 11')
        break
else:
    print('Это число может быть представлено в системе счисления с основанием меньше 11')
 
