name = input('Введите раширение имени файла')
if name == 'htm' or name == 'html' or name == 'php':
    print('Это веб-страница')
elif name == 'doc' or name == 'docx' or name == 'txt':
    print('Это текстовый документ')
elif name == 'py':
    print('Это программа на Python')
else:
    print('Это что-то другое')
