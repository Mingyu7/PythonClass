def print_something(a):
    print(a)
p = print_something
p(123) #함수를 변수에 담아 사용할 수 있다
p('abc')

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b

flist = [plus,minus] ##함수를 리스트의 요소로 집어넣기
#각각 함수 위치에서 매개변수 입력시 함수 출력
flist[0](1,2) 
flist[1](1,2)

def hello_korean():
    print('안녕하세요')
def hello_english():
    print('hello')
def greet(hello):
    hello()
#함수는 다른 함수의 매개변수로 사용가능
greet(hello_korean)
greet(hello_english)

def get_greeting(where):
    if where =='K':
        return hello_korean
    elif where == 'E':
        return hello_english

get_greeting('K')
get_greeting('E')

import math
def stddev(*args):
    def mean(): #중첩함수
        return sum(args)/len(args)

    def variance(m):
        total = 0
        for arg in args:
            total += (arg - m) ** 2
        return total/(len(args)-1)
        
    v = variance(mean())
    return print(math.sqrt(v))

stddev(2.3,1.7,1.3,0.7,1.8)

## 파이썬은 pass 키워드를 이용해 빈 함수나 클래스를 만들수 있다
def ex():
    pass

class empty_class:
    pass 
