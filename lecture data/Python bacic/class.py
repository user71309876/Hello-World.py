###################################################################
#class(c의 구조체 비스무리한거),__init__(생성자),member varialbe
class Unit:
    def __init__(self, name, hp, damage):#self는 자기 자신
        self.name=name
        self.hp=hp#이것들이 맴버 변수
        self.damage=damage#맴버 변수는 파란색임
        print(f"{self.name} is product")
        print(f"hp : {self.hp}, damage : {self.damage}")

mar1=Unit("marine",40,5)
mar2=Unit("marine",40,5)
tank=Unit("탱크",150,35)

war1=Unit("race",80,50)
war2=Unit("stolen race",80,50)
war2.clocking=True

if war2.clocking==True:#새로운 맴버 변수를 만들 수도 있음
    print(f"{war2.name} is clocking")
# if war1.clocking==True:#다만 war2에서만 clocking 변수가 있음
#     print(f"{war1.name} is clocking")

print("\n\n\n")

###################################################################
#method
class AttackUnit:
    def __init__(self, name, hp, damage):#이곳은 class 내부에서 변수를 저장하는 곳
        self.name=name#이것들이 맴버 변수
        self.hp=hp
        self.damage=damage
        print(f"{self.name} is product")
        print(f"hp : {self.hp}, damage : {self.damage}")

    def attack(self,location):#메소드 : class 내부에서 함수를 선언
        self.location=location#맴버변수 저장도 가능하네요
        print(f"{self.name} : attacking at {location}. [power {self.damage}]")

    def damaged(self,damaged):#매소드는 노란색으로 나타남
        print(f"{self.name} : Be attacked {damaged}. [power {self.damage}]")
        self.hp-=damaged
        print(f"{self.name} : hp is {self.hp}")
        if self.hp<=0:
            print(f"{self.name} : destoryed")

firebat1=AttackUnit("firebat",50,16)
firebat1.attack("5")
firebat1.damaged(25)#매소드를 출력할때도 노란색임
firebat1.damaged(25)
print(firebat1.location)

print("\n\n\n")

###################################################################
#inheritance(상속)
class Unit:#여기에 있는 맴버 변수를 AttackUnit에서도 쓸 수 있게 함. 그게 상속
    def __init__(self, name, hp):
        self.name=name
        self.hp=hp


class AttackUnit(Unit):#괄호 안에 클래스 이름 넣고
    def __init__(self, name, hp, damage):
        Unit.__init__(self,name,hp)#이렇게 정의해줍니다
        self.damage=damage
        print(f"{self.name} is product")
        print(f"hp : {self.hp}, damage : {self.damage}")

    def attack(self,location):
        self.location=location
        print(f"{self.name} : attacking at {location}. [power {self.damage}]")

    def damaged(self,damaged):
        print(f"{self.name} : Be attacked {damaged}. [power {self.damage}]")
        self.hp-=damaged
        print(f"{self.name} : hp is {self.hp}")
        if self.hp<=0:
            print(f"{self.name} : destoryed")

#이때 상속해주는 클래스를 부모 클래스(Unit)
#상속을 받는 클래스를 자식 클래스라 함(AttackUnit)

print("\n\n\n")

###################################################################
#mutiple inheritance(다중 상속)
class Flyable:
    def __init__(self,fly_speed):
        self.fly_speed=fly_speed
    def fly(self,name,location):
        print(f"{name} : fly to {location}. [speed {self.fly_speed}]")

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,fly_speed)

valkyrie=FlyableAttackUnit("valkyrie",200,6,5)
valkyrie.fly(valkyrie.name,3)

print("\n\n\n")

###################################################################
#method overriding(메소드 오버라이딩)
#부모 클래서에서 정의된 메소드를 자식 클래스에서 재정의하는것

class Unit:#여기에 있는 맴버 변수를 AttackUnit에서도 쓸 수 있게 함. 그게 상속
    def __init__(self, name, hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
    
    def move(self, location):
        print("[ground unit move]")
        print(f"{self.name} : move in the {location} direction [speed {self.speed}]")

class AttackUnit(Unit):#괄호 안에 클래스 이름 넣고
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name,hp, speed)#이렇게 정의해줍니다
        self.damage=damage
        print(f"{self.name} is product")
        print(f"hp : {self.hp}, damage : {self.damage}")

    def attack(self,location):
        self.location=location
        print(f"{self.name} : attacking at {location}. [power {self.damage}]")

    def damaged(self,damaged):
        print(f"{self.name} : Be attacked {damaged}. [power {self.damage}]")
        self.hp-=damaged
        print(f"{self.name} : hp is {self.hp}")
        if self.hp<=0:
            print(f"{self.name} : destoryed")

class Flyable:
    def __init__(self,fly_speed):
        self.fly_speed=fly_speed
    def fly(self,name,location):
        print(f"{name} : fly to {location}. [speed {self.fly_speed}]")

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage,fly_speed):#0을 넣으면 speed 안넣어줘도 됨
        AttackUnit.__init__(self,name,hp,0,damage)#Unit의 speed 값을 이렇게 정의할 수도 있음
        Flyable.__init__(self,fly_speed)
    def move(self,location):
        print("[move midair unit]")
        self.fly(self.name,location)

vulture=AttackUnit("valture",80,10,20)

battle=FlyableAttackUnit("battle",500,25,3)

vulture.move(11)
battle.fly("battle",9)
#지상이든 공중이든 다 move 함수 쓰고 싶어요
#그래서 전 메소드 오버라이딩을 쓸 거에요
battle.move(9)

print("\n\n\n")

###################################################################
#pass
class BulidingUnit(Unit):
    def __init__(self,name,hp,location):#원래같았으면 오류가 났지만 pass를 씀으로 일단 넘어간다는 의미
        pass
    
sup_depot=BulidingUnit("supply depot",500,7)#에러가 안나는 모습

print("\n\n\n")

###################################################################
#super
class BulidingUnit(Unit):
    def __init__(self,name,hp,location):
        #Unit.__init__(self,name,hp, 0)
        super().__init__(name,hp,0)
        #위에위에줄과 같은 의미로 Unit class를 상속받은 모습
        #self는 쓰지 않는다
        #다중상속일때는 쓰지 않는다
        self.location=location