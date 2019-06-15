import math
def HDM(beg:"Начало отрезка",end:"Конец отрезка",eps:"Точность",f:"Функция") -> "Находит x " :
	"""
        Метод половиного деления
	>>> round(HDM(-5,-1,0.01,lambda x : x ** 2 + 4 * x -3),2)
	-4.64
	>>> round(HDM(-1,5,0.01,lambda x : x ** 2 + 4 * x -3),2)
	0.64
	"""
	while abs (beg - end) > eps :
		c = (beg + end) / 2
		d = f(c) * f(beg)
		if d > 0 :
			beg = c
		else:
			end = c
	return (beg + end)/ 2
v = 10
h = 1
l = 7
H = 5
print(HDM(0,90,0.01,lambda x: (h+v*math.sin(x)*(l/(v*math.cos(x)))-((9.8*l**2)/(2*(v**2)*(math.cos(x)**2)))-H)))
