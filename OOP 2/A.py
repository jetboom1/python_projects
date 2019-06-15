class Road():
    def __init__(self,length0,width0):
        self.length = length0
        self.width = width0
class Car():
    def __init__(self, road0: object, linepos0: int, velocity0: int) -> object:
        self.road = road0
        self.linePos = linepos0
        self.velocity = velocity0
        self.x = 0
    def move(self):
        self.x+=self.velocity
        if self.x>self.road.length:
            self.x = 0
    def draw(self):
        print(('-'*self.x)+'C'+('-'*(self.road.length-self.x)))
road = Road(100,3)
n = 3
cars = []
for i in range(n):
    cars.append(Car(road,i+1,(i+1)*3))
for k in range(50):
    print()
    for i in range(n):
        cars[i].move()
        cars[i].draw()