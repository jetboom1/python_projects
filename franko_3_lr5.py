from math import cos
x=float(input('x= '))
e=float(input('eps- '))
a=s=x
n=1
while abs(a)>e:
    a=-a*x*x/(2*n+1)/(2*n)
    n+=1
    s+=a
print('n-',n,'s-',round(s+a,4),'sin(x)-',round(sin(x),4),'ошибка-', round(s+a-sin(x) ,4))
