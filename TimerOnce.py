import threading
import datetime

def function_a():
    print("현재시간")
    print(datetime.datetime.now())

print(datetime.datetime.now())
threading.Timer(10,function_a).start() #10초후 function_a함수 실행할 Timer생성하고 start()호출