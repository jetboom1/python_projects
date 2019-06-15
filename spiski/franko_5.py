'''Заполните массив из 10 элементов случайными числами в
интервале [0,100] и подсчитайте отдельно среднее значение всех
элементов, которые <50, и среднее значение всех элементов,
которые ≥50.'''
from random import randint
summary1 = 0
summary2 =0
count1 = 0
count2=0
array = [0]*10
array = [randint(0,100) for i in array]
for i in array:
    print(i, end=' ')
    if i<50:
        count1+=1
        summary1+=i
    else:
        count2+=1
        summary2+=i
print('\nСреднее арифметическое чисел меньших 50:', summary1/count1,'\nА среднее арифметическое чисел >=50:',summary2/count2)