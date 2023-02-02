with open('movie_quotes.txt','r') as file:
    line = file.readline() #파일 한줄씩 읽기

    while line != '': #readline은 파일끝에 ''을 반환하는데 실제로 빈 줄일경우 개행문자 반환
        print(line,end='')
        line = file.readline() 