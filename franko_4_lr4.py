name,ext = input('Введите имя файла').split('.')
if ext == 'htm' or ext == 'html' or ext == 'php':
    print('Это веб-страница')
elif ext == 'doc' or ext == 'docx' or ext == 'txt':
    print('Это текстовый документ')
elif ext == 'py':
    print('Это программа на Python')
else:
    print('Это что-то другое')
