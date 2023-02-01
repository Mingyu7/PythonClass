my_list = [1,2,3]

try: 
   #문제 없을때 실행
except:
    #문제 발생시 실행

#복수개의 except 사용
try:
    print("첨자를 입력하세요.")
    index = int(input())
    print(my_list[index]/0)
except ZeroDivisionError: 
    print('0으로 나눌수없음')
except IndexError:
    print('잘못된 첨자입니다')