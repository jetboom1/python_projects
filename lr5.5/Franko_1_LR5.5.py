x = float(input('Введите x'))
numerator = 1
denominator = 1
if x%2==1 and x<=63:
    print('Вы не можете делить на ноль')
else:
    for i in range(2,66,2):
        numerator = numerator*(x-i)
    for i in range(1,65,2):
        denominator = denominator*(x-i)
    result = numerator/denominator
    print('Результат',result)
    
