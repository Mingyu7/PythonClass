#직접 대입
s1= 'name : {0}'.format('Block')
print(s1)

#변수로 대입
age = 22
s2 = 'age : {0}'.format(age)
print(s2)

#이름으로 대입
s3 = 'number : {num}, gender : {gen}'.format(num=22,gen='남')
print(s3)
print("\n")

'''인덱스 가지고 놀기'''
#인덱스 없음
s4 = 'name : {}, city : {}'.format('min','korea')
print(s4)

#인덱스 순서 변경
s5 = 'song1 : {1}, song2 : {0}'.format('nana','ice cream')
print(s5)

#인덱스 중복
s6 = 'test1:{0}, test2:{1},test3:{0}'.format('in0','in1')
print(s6)
print("\n")

'''중괄호 출력'''
#중괄호 출력
s7 = 'hello world{{}},{}'.format('text1')
print(s7)

#중괄호 안에 문자 출력
s8 = 'hello {{{0}}}'.format('mingyu')
print(s8)
print("\n")

'''문자열 정렬'''
#왼쪽 정렬
s9 = 'this is {0:<10} | done {1:<10} |'.format('left','a') #10자리 표현 왼쪽정렬
print(s9)

#오른쪽 정렬
s10 = 'this is {0:>7} | done {1:>7} |'.format('right','b') #7자리 표현 오른쪽 정렬
print(s10)

#가운데 정렬
s11 = 'this is {0:^5} | done {1:^5} |'.format('center','c') #5자리 표현 가운데 정
print(s11)
print("\n")

'''문자열에 공백 부분 채우기'''
#공백부분에 -기호 채우기
s12 = 'this is {0:-<10} | done {1:o<5} |'.format('left', 'a') 
print(s12)

#공백부분에 +기호 채우기
s13 = 'this is {0:+>10} | done {1:0>5} |'.format('right', 'b') 
print(s13) 
 
#공백부분에 .기호 채우
s14 = 'this is {0:.^10} | done {1:@^5} |'.format('center', 'c')
print(s14)



                                             
                                             
