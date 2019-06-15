class Road():
    def __init__(self,length0,width0):
        self.length = length0
        self.width = width0


class Car():
    def __init__(self, road0,tlight0, linepos0, velocity0):
        self.road = road0
        self.tlight = tlight0
        self.linePos = linepos0
        self.velocity = velocity0
        self.x = 0

    def move(self):
        if self.tlight.x - self.x < 4 and self.tlight.x - self.x > 0:
            if self.tlight.currentSignal== 'G':
                self.x+=self.velocity
        else:
            self.x += self.velocity
        if self.x>self.road.length:
            self.x = 0

    def draw(self):
        print(('-'*self.x)+'C'+('-'*(self.road.length-self.x)))


class TrafficLight:
    def __init__(self,road0,x0,y0,signalTime0):
        self.road = road0
        self.x = x0
        self.y = y0
        self.currentSignal = 'R'
        self.signalTime = signalTime0

    def changeTheLight(self):
        if self.currentSignal == 'R':
            self.currentSignal = 'G'
        else:
            self.currentSignal = 'R'

    def draw(self):
        print((' '*self.x)+self.currentSignal+(' '*(self.road.length-self.x)))


road = Road(100,3)
n = 3
cars = []
trafficlights = []
for i in range(n):
    trafficlights.append(TrafficLight(road,(i+2)**3,i+1,(i+5)*2))
    cars.append(Car(road,trafficlights[i],i+1,(i+1)*3))
for k in range(100):
    print()
    for i in range(n):
        if k % trafficlights[i].signalTime == 0:
            trafficlights[i].changeTheLight()
        trafficlights[i].draw()
        cars[i].move()
        cars[i].draw()