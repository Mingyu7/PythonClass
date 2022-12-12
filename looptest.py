#while 반복문
print ("몇번 반복할까요?")
limit=int(input()) #정수로 입력 받음
count=0

while count<limit:
    count+=1
    print("{0}회 반복..".format(count))
print("반복이 종료되었습니다.")
print("-----------------------")
while 1:
    print("반복할까요? 예/아니요 ")
    ans=(input())
    if ans=="예":
        print("반복중..")
    elif ans=="아니요":
        print("종료중..")
        break
    else:
        print("잘못 입력하셨네요")
print("종료되었습니다..")

#for 반복문
for i in["가","나다","다"]: #순서열 순서대로 출력
 print(i)
print("\n")

for s in'뇌를 자극하는 파이썬': #하나씩 나누어 출력
    print(s)
print("\n")

for num in range(0,5,1): #시작값,멈춤값,두수의차
    print(num)
print("\n")

for num1 in range(0,10,2): #2의 배수만 출력
    print(num1)
print("\n")

for num2 in range(10): #홀수만 출력
    if num % 3==0: #홀수일때 continue
        continue
    print(num2)
print("\n")

for num3 in range(100): #100까지 반복중 25가되면 반복문 탈출
    print(num3)
    if num3==25:
        print("종료")
        break






    
