counter=0
summary = 0
array = [0]*5
data = int(input().split())
array = list(data)
for i in array:
    summary += i
    counter+=1
print('Среднее арифметическое равно', summary/counter)

