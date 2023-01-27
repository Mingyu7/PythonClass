class Base:
    def base_method(self):
        print("base_method")
    def test_print(self):
        print("test")

class Derived(Base): #클래스상속을 하려면 클래스명(상속할 클래스)
    pass

class A:
    def __init__(self):
        print("A.__init__()")
        self.message = "Hello"  

class B(A):
    def __init__(self):
        print("B.__init__()")

        super().__init__() #부모 클래스의 인스턴스를 가져오기 위해서 super() 사용
        print('self.message is'+self.message)

class C:
    pass

class D(A,C): #다중상속은 이렇게 ,로 묶어서 상속한다
    pass

#Overrriding
class Q:
    def method(self):
        print('Q')

class W(Q):
    def method(self):
        print('W')

class E(Q):
    def method(self):
        print('E') 

class Car:
    def ride(self):
        print('Run!')
class FlyingCar(Car):
    def ride(self):
        super().ride() #super()사용해서 오버라이딩을 했다
        print("Fly!")

Q().method()
W().method()
E().method()
my_car = FlyingCar()
my_car.ride()
print("--------")

der = Derived()
der.base_method()
der.test_print()
print("--------")
if __name__ == "__main__":
    b=B()