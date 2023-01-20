class InstanceCounter:
    count = 0
    def __init__(self):     #인스턴스 생성마다 count에 1증가
        InstanceCounter.count+=1

    @classmethod
    def print_instance_count(cls): # @classmethod 는 cls 매개변수가 필수다
        print(cls.count)
if __name__ == "__main__":
    a = InstanceCounter() #첫번째 생성
    InstanceCounter.print_instance_count()

    b = InstanceCounter() #두번째 생성
    InstanceCounter.print_instance_count()

    c = InstanceCounter() #세번째 생성
    c.print_instance_count()