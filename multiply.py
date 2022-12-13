for i in range(2,10,1):
    for j in range(1,10,1):
        print('{} * {} = {}'.format(i,j,i*j))
    print(sep='\n') #한줄 띄기

while True:
    print('몇단을 출력할까요? 끝 입력시 종료')
    
    num=input()
    if num == '끝':
        print('종료 되었습니다')
        break
    else:
        num=int(num)
        for i in range(1,10,1):
            print('{0} * {1} = {2:2}'.format(num,i,num*i))
    
