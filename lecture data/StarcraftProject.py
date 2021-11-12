from random import *

class Unit:
    def __init__(self, name, hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
    
    def move(self, location):
        print("[ground unit move]")
        print(f"{self.name} : move in the {location} direction [speed {self.speed}]")
        
    def damaged(self,damaged):
        print(f"{self.name} : Be attacked {damaged}. [power {self.damage}]")
        self.hp-=damaged
        print(f"{self.name} : hp is {self.hp}")
        if self.hp<=0:
            print(f"{self.name} : destoryed")

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp, speed)
        self.damage=damage
        print(f"{self.name} is product")
        print(f"hp : {self.hp}, damage : {self.damage}")

    def attack(self,location):
        self.location=location
        print(f"{self.name} : attacking at {location}. [power {self.damage}]")

class Flyable:
    def __init__(self,fly_speed):
        self.fly_speed=fly_speed
    def fly(self,name,location):
        print(f"{name} : fly to {location}. [speed {self.fly_speed}]")

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage,fly_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,fly_speed)
    def move(self,location):
        print("[midair unit move]")
        self.fly(self.name,location)
  
        
#마린 클래스 만들기
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"Marine",40,1,5)
    #stimpack
    def StimPack(self):
        if self.hp>10:
            self.hp-=10
            print(f"{self.name} using stimpack (reduce 10 hp)")
        else:
            print(f"{self.name} is health is low")
            
class Tank(AttackUnit):
    seize_developed=False
    
    def __init__(self):
        AttackUnit. __init__(self,"Tank",150,1,35)
        self.seize_mode=False
        
    def Set_seize_mode(self):
        if Tank.seize_developed==False:
            print("size mode is not develop")
            return
        if self.seize_mode==False:
            print(f"{self.name} : transform to the size mode")
            self.damage*=2
            self.seize_mode=True
        else:
            print(f"{self.name} : turn off the size mode")
            self.damage/=2
            self.seize_mode=False           
                    
class Wraith(FlyableAttackUnit):    
    def __init__(self):
        FlyableAttackUnit.__init__(self,"Wraith",80,20,5)
        self.clocked=False
    
    def clocking(self):
        if self.clocked==True:
            print(f"{self.name} : turn off clocking mode")
            self.clocked=False
            
        if self.clocked==False:
            print(f"{self.name} : turn on clocking mode")
            self.clocked=True
        
def game_start():
    print("[Notice] new name will be start")
    
def game_over():
    print("Player : gg")
    print("[player] exit the game")
    
game_start()

m1=Marine()
m2=Marine()
m3=Marine()

t1=Tank()
t2=Tank()

w1=Wraith()

attack_unit=[]
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

for unit in attack_unit:
    unit.move(1)
    
Tank.seize_developed=True
print("[Notice] : Tank seize mode is developed")

for unit in attack_unit:
    if isinstance(unit,Marine):
        unit.StimPack()
    elif isinstance(unit,Tank):
        unit.Set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

for unit in attack_unit:
    unit.attack(1)
    
for unit in attack_unit:
    unit.damaged(randint(5,20))
    
game_over() 