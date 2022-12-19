for i in range(10):
    if i % 2 ==0:
        continue #i가 짝수일때 그반복 건너뛰기
    print(i)
print("\n")
i = 0
while True:
    i+=1
    if i == 10:
        print("i가{}이 되었습니다 반복을 중단 합니다.".format(i))
        break #i가 홀수일떄 반복문 중단
    print(i)