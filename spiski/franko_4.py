'''Введите массив из 5 элементов с клавиатуры и найдите
среднее арифметическое его значений.'''
counter=0
summary = 0
data = input().split()
array = list(map(int,data))
for i in array:
    summary += i
    counter+=1
print('Среднее арифметическое равно', summary/counter)
