'''Создать список, каждый элемент которого равен квадрату своего номера.'''
a = [i*i for i in range (10)]
for i in a:
    print(i,end=' ')