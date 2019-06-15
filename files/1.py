with open('pi.txt') as file:
    birthdate = input('Введите дату своего рождения в формате ддммгггг или свой номер телефона')
    lines = file.readlines()
    piString = ''
    for i in lines:
        piString += i.strip()
    if piString.count(birthdate)>0:
        print('Ваша дата рождения или номер телефона встречаются в 4 миллионах знаках Пи {0} раз'.format(piString.count(birthdate)))
    else:
        print('Удивительно, ваша последовательность не встречается в первых 4 миллионах знаках числа Пи')