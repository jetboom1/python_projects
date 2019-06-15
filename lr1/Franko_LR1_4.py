# Ввести три числа: цену пирожка (два числа: гривны, потом – копейки) и количество
# пирожков. Найти сумму, которую нужно заплатить (гривны и копейки)
boolean = 1
uah = int(input("Введите гривны "))
coins = int(input("Введите копейки "))
num = int(input('Количество? '))
coins_summary = coins*num
uah_summary = uah*num
while boolean==1:
    if coins_summary>=100:
        coins_summary-=100
        uah_summary+=1
        #print('С вас', uah_summary,'UAH', coins_summary, 'копеек')
    else:
        print('С вас', uah_summary,'UAH', coins_summary, 'копеек')
        break
