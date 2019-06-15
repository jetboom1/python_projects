n = int(input('Введите n'))
a=1
b=1
c=1
for i in range(0, n):
  a = 2*i+1
  b = 2*i+2
  c *= a/b
print(c)
