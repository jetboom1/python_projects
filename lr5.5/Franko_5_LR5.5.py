n=int(input('Введите n'))
a=1
b=1
c=1
for i in range(1,n+1):
	d=a/b
	a=2*i+1
	b=b+1
	c=c*d
print(c)
