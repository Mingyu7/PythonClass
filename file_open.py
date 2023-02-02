file = open("test.txt",'w') #test.txt 파일 생성
file.write('hello') # 파일에 hello작성
file.close() #닫기

file = open("test.txt",'r') #test.txt 파일 읽기
str = file.read() #str에 파일 저장
print(str) #출력
file.close() #닫기