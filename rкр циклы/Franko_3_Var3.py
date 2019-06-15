'''Преобразовать строку, вводимую пользователем, заменив в ней все
восклицательные знаки точками.'''
string = input('Введите строку')
result=''
for i in string.split('!'):
    result = result+i+'.'
print(result)
