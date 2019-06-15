string = input('Введите строку ')
save = ''
counter = 1
result=''
while string!='':
    save = string[0]
    string = string[1:]
    if string == '':
        result = result+save+str(counter)
        break
    elif save==string[0]:
        counter+=1
    else:
        result = result+save+str(counter)
        counter = 1
print(result)
