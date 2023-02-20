from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("600x480") 

txt = Text(root,width=30,height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요") #기본값 제공


e = Entry(root,width=30) #한줄로 입력받을때
e.pack()
e.insert(0,"한 줄만 입력해요")


def btncmd():
    #내용 출력
    print(txt.get("1.0",END)) #처음부터 끝까지 출력 1 : 첫번째 라인 0 : 0번째 colnum위치 
    print(e.get())
def btncmd1():
    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root,text="클릭",command=btncmd)
btn.pack()
btn1 = Button(root,text="삭제",command=btncmd1)
btn1.pack()

root.mainloop()