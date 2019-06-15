string = input('Введите имя переменной')
for i in string:
    if i.isdigit()==False and i.isalpha()==False and i != '_':
        print('Это не может быть именем переменной')
        break
else:
    if string[0].isdigit()!=False:
        print('Это не может быть именем переменной')
    else:
        print('Это может быть именем переменной')
    
