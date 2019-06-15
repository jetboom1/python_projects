string = input('Введите строку ')
save = ''
number = 0
result=''
while string!='':
    number = int(string[1])
    save = string[0]
    string = string[2:]
    result=result+(save*number)
print('Расшифрованная строка:',result)
