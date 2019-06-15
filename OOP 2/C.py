from random import randint
class Soldier:
    def makeHealth(self, value):
        self.health = value
    def makeKick(enemy):
        if randint(0,20)==20:
            enemy.health = 0
            print('НОКАУТ!!!')
        else:
            enemy.health -= randint(5,20)
class Battle:
    def battle(self, u1, u2, u3, u4):
        while u1.health > 0 or u2.health > 0 or u3.health > 0 or u4.health > 0:
            n = randint(1,4)
            k = randint(1,4)
            if k ==1:
                target = u1
            if k==2:
                target = u2
            if k ==3:
                target = u3
            if k==4:
                target = u4
            print("{0} бьет {1}".format(n,k))
            Soldier.makeKick(target)
            print("У {0} осталось".format(k),target.health)
            print()
            if u1.health <= 0 or u2.health <= 0 or u3.health <= 0 or u4.health <= 0:
                break
        if u1.health >0 and u2.health <=0 and u3.health <=0 and u4.health <=0:
            self.result = "ПЕРВЫЙ ПОБЕДИЛ"
        elif u1.health <=0 and u2.health >0 and u3.health <=0 and u4.health <=0:
            self.result = "ВТОРОЙ ПОБЕДИЛ"
        elif u1.health <=0 and u2.health <=0 and u3.health >0 and u4.health <=0:
            self.result = "ТРЕТИЙ ПОБЕДИЛ"
        elif u1.health <=0 and u2.health <=0 and u3.health <=0 and u4.health >0:
            self.result = "ЧЕТВЕРТЫЙ ПОБЕДИЛ"
        else:
            self.battle(u1, u2, u3, u4)
    def whoWin(self):
        print(self.result)


first = Soldier()
second = Soldier()
third = Soldier()
fourth = Soldier()
first.makeHealth(100)
second.makeHealth(100)
third.makeHealth(100)
fourth.makeHealth(100)
b = Battle()
b.battle(first, second,third,fourth)
b.whoWin()
