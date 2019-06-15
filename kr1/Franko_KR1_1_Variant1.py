x = float(input('Введите первое число'))
y = float(input('Введите второе число'))
z = float(input('Введите третье число'))
if x+y+z<1 and x<y and y<z:
    x = (y+z)/2
    print(x,y,z)
if x+y+z<1 and y<x and x<z:
    y = (z+x)/2
    print(x,y,z)
if x+y+z<1 and z<y and y<x:
    z = (y+x)/2
    print(x,y,z)
if x+y+z>=1 and x<y:
    x = (y+z)/2
    print(x,y,z)
else:
    y = (x+z)/2
    print(x,y,z)
        
