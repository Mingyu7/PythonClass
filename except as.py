my_list2 = [1,2,3]
try:
    print("첨자를 입력하세요.")
    index2 = int(input())
except ZeroDivisionError as err: #as 를사용하면 예외의 인스턴트를 얻어낼수있다 사용법 as (변수명)
    print("0으로 나눌수 없습니다. ({0})".format(err))
except IndexError as err:
    print("잘못된 첨자 입니다. ({0})".format(err)) 