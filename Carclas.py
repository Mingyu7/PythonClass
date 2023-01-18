class Car:
    def __init__(self): #__init__은 초기화를 담당
        self.color = 0xFF0000 #바디의 색
        self.wheel_size = 16 #바퀴의 크기
        self.displacement = 2000 #엔진 배기량s

    def forward(self): #전진
        pass
    def backward(self): #후진
        pass
    def turn_left(self): #좌회전
        pass
    def turn_right(self): #우회전
        pass
#Car 클래스 정의 종료. 아래는 Car클래스의 인스턴스를 정의하고 사용하는 코드

if __name__ == '__main__':
    my_car=Car()

    #my_car 정보 출력
    print('0X{:02X}'.format(my_car.color))
    print(my_car.wheel_size)
    print(my_car.displacement)

    #my_car 메소드 호출
    my_car.forward()
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()