from abc import ABCMeta
from abc import abstractmethod
class AbstractDuck(metaclass = ABCMeta):
    @abstractmethod
    def Quack(self):
        pass

#class Duck(AbstractDuck): !Error!
    #pass

class Duck(AbstractDuck): #추상메소드를 형식이 맞게 작성해야한다
    def Quack(self):
        print("[Duck] Quack")

duck = Duck()
duck.Quack()