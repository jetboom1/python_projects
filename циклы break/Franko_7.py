import random
#num = str(random.randint(1000,9999))
num = str(1225)
usernum = 0
counter = 0
bulls = 0
cows = 0
while num!=usernum:
    usernum = input('Введите ваше число')
    for i in num:
        if num.find(i) != -1:
            for a in usernum:
                if a==i:
                    bulls+=1
            else:
                cows+=1
    print('Коров:',cows,'\n','Быков:',bulls)
    bulls = 0
    cows = 0
    counter+=1
print('ПОЗДРАВЛЯЕМ!\nВЫ УГАДАЛИ ЧИСЛО ЗА',counter,'попыток')
