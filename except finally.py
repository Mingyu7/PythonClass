my_list2 = [1,2,3]
try:
    print("첨자를 입력하세요.")
    index2 = int(input())
    print("my_list2[{0}]: {1}".format(index2,my_list2[index2]))
except Exception as err: 
    print("예외가 발생했습니다 . ({0})".format(err))
finally: #무조건 실행
    print("어떤 일이 있어도 마무리 합니다.") 