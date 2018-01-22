#handle an exception
while True:
    try:
        number = int(input("What's your fav number hoss?\n"))
        print(18/number)
        break
    except ValueError:  #if the input is a string
        print("Make sure and enter a number")
    except ZeroDivisionError:  #if the input is a zero
        print("Don't pick zero")
    except:  #not a good idea and most probably hide problems
        break
    finally:  #execute this no matter what, occurs every single time
        print("loop complete")



#classes and objects
class Enemy:
    life = 3
    def attack(self):
        print("Ouch!")
        self.life-=1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life)+" life left")

enemy1 = Enemy() #create object called  enemy1
enemy2 = Enemy() #create another object called enemy2
enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()


#init function
class Person:
    def __init__(self):
        print("Mary")
    def swim(self):
        print("I am coding")

#init function is executed even though it is not called no matter what
#looking for init function to execute it
human1 = Person()
human1.swim()


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

#pass the 5 and 18 parameters to x
jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()


#class and instance variable
class Girl:

    # gender is a class variable
    # all people are females
    gender = "female"
    def __init__(self,name):
        # each female has different name
        # instance variable
        self.name = name

r = Girl("Rachel")
s = Girl("Stanky")
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)


#inheritance
class Parent():
    def print_last_name(self):
        print("Chew")

class Child(Parent):   #inherit from Parent
    def print_first_name(self):
        print("Mary")

    #overriding method
    def print_last_name(self):
        print("Tan")

mary = Child()
mary.print_first_name()
mary.print_last_name()


#multiple inheritance
class Mario():
    def move(self):
        print("I am moving")

class Shroom():
    def eat_shroom(self):
        print("Now I am big")

class BigMario(Mario,Shroom):  #inherit from Mario and Shroom
    pass   #no need to rewrite the same code

bm = BigMario()
bm.move()
bm.eat_shroom()


#threading
import threading

class MarysMessenger(threading.Thread):
    def run(self):
        #put underscore if you want any kinds of number no matter what
        for _ in range(10):
            print(threading.current_thread().getName())

x = MarysMessenger(name="Send out messages")
y = MarysMessenger(name="Receive messages")

#run at the same time using thread
x.start()
y.start()




