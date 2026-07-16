from abc import ABC, abstractmethod
class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("I can walk and run")
    
class Snake(Animal):

    def move(self):
        print("I can crawl")

class dog(Animal):
    
    def move(self):
        print("I can bark")

class lion(Animal):

    def move(self):
        print("I can roar")

R = Human()
R.move()

K = Snake()
K.move()

R = dog()
R.move()

K = lion()
K.move()


    