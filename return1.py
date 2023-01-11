def ogamdo(num):
    for i in range(1,num+1):
        print('제 {0}의 아해'.format(i))
        if i ==5:
            return ##반환 데이터없이는 함수 종료 의미로 사용

def print_something(*args):
    for s in args:
        print(s)


ogamdo(3)
print_something(1,2,3,4)