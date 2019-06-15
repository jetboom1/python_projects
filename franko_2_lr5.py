print('************************\nДОБРО ПОЖАЛОВАТЬ\n************************\nВ САМУЮ ЗАМЕЧАТЕЛЬНУЮ\n************************\nКОМПЬЮТЕРНУЮ ИГРУ НА PYTHON\n************************\nГТА 6 ОТ МИРА ВИДЕОИГР\n************************\nОТ НИКОМУ НЕ НУЖНОГО РАЗРАБОТЧИКА\n************************\nНАЙДИ СУММУ НЕЧЕТНЫХ ЧИСЕЛ И ПРОИЗВЕДЕНИЕ ЧЕТНЫХ\n************************\nНАЖМИТЕ y чтобы продолжить\n')
confirm = input()
sum_counter = 0
mult_counter = 0
summary = 0
multiplication = 1
if confirm == 'y':
    usernum = int(input('Введите число'))
    while usernum!=55555:
        if usernum%2==0 or usernum==0:
            multiplication = multiplication*usernum
            usernum = int(input('Введи следующее число'))
            sum_counter+=1
        else:
            summary = summary + usernum
            usernum = int(input('Введи следующее число'))
            mult_counter+=1
    print('Поздравляю, сумма нечетных чисел равна', summary,', а произведение четных -', multiplication,'.\nПри этом кол-во множителей равно',mult_counter,', а кол-во слагаемых',sum_counter)
else:
    print('На нет и суда нет')
