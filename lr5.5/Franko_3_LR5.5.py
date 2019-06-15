n = int(input('Введите n'))
if n%2==0:
    for i in range(2,n,2):
        result = i*(i+2)
else:
    for k in range(1,n+1,2):
        result = k*(k+2)
print(result)
