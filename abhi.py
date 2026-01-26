class phone:
    def make_call(self):
        print("making phone call")
    def play_game(self):
        print("playing game")
p1=phone()
p1.make_call()
p1.play_game()

class Phone:

    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

    def make_call(self):
        print("Making phone call")

    def play_game(self):
        print("Playing Game")

class emp:
    def __init__(self,name,age,salary,gendr ):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gendr
    def emp_details(self):
        print("name of emp is",self.name)
        print("age of emp is",self.age)
        print("salary of emp is",self.salary)
        print("gender of emp is",self.gender)
e1=emp("abhi",21,21000,"male")
e1.emp_details()

class vehicle:
    def __init__(self,milage,cost):
        self.milage=milage
        self.cost=cost
    def show_details(self):
        print("i am a vehicle")
        print("milage of vehicle is",self.milage)
        print("cost of vehicle is",self.cost)
v1=vehicle(500,500)
v1.show_details()

class car(vehicle):
    def show_car(self):
        print("i am a car")
c1=car(200,12000)
c1.show_details()
c1.show_car()

class car(vehicle):
    def __init__(self, milage, cost,tyres,hp):
        super().__init__(milage, cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("i an a car")
        print("number of tyres are",self.tyres)
        print("value of horse power is",self.hp)
c1=car(20,12000,4,300)
c1.show_details()
c1.show_car_details()

class parent1():
    def assign_string_one(self,str1):
        self.str1=str1
    def show_string_one(self):
        return self.str1
class parent2():
    def assign_string_two(self,str2):
        self.str2=str2
    def show_string_two(self):
        return self.str2
class derived(parent1,parent2):
    def assign_string_three(self, str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3
    
d1=derived()
d1.assign_string_one("one")
d1.assign_string_two("two")
d1.assign_string_three("three")

d1.show_string_one()
d1.show_string_two()
d1.show_string_three()

class parent():
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        return self.name

class child(parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        return self.age
    
class grandchild(child):
    def assign_gender (self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender
    
g1=grandchild()
g1.assign_name("sam")
g1.assign_age("24")
g1.assign_gender("male")

g1.show_name()
g1.show_age()
g1.show_gender()