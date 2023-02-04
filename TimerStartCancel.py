import threading

count =0

def on_timer():
    global count
    count+=1
    print(count)

    timer = threading.Timer(1,on_timer)
    timer.start()

    if count == 10:
        print("Canceling timer...")
        timer.cancel() #종료

print("Starting timer..")
on_timer()

#위에코드보다 간결 timer.cancel() 안써도 10이 되면 자동 종료
'''if count < 10:
   timer = threading.Timer(1,on_timer) 
   timer.start()
'''
