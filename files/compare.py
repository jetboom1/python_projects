name1 = input('введите имя первого файла')
name2 = input('введите имя второго файла')
flag = False
with open(name1, 'r') as fileOne:
    with open(name2, 'r') as file2:
        lines1 = fileOne.readlines()
        lines2 = file2.readlines()
        for line1 in range(len(lines1)):
            for line2 in range(len(lines2)):
                if line1!=line2:
                    continue
                else:
                    if lines1[line1].lower().strip() != lines2[line2].lower().strip():
                        print('Строки не совпадают! Строка первого файла: {0}\nСтрока второго файла: {1}'.format(lines1[line1], lines2[line2]))
                        flag = True
        if flag == False:
            print('Файлы совпали!')
