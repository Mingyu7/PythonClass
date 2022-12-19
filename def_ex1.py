def my_abs(arg):
    if(arg<0):
        result = arg* -1
    else:
        result = arg
        
    return print(result)

def print_string(text,count):
    for i in range(count):
        print(text)

def print_string2(text,count=1): #매개변수 값을 지정해주면 기본값이 된다
    for i in range(count):
        print(text)

def print_personnel(name,position ='staff',nationality='Korea'): #키워드 매개변수
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))

def merge_string(*text_list): #가변매개변수 *변수 개수가 유동적이다
    result=''
    for s in text_list:
        result+=s
    return print(result)

def print_team(**player): # 가변매개변수에서 *을 하나더 붙이면 딕셔너리 가변매개변수가 된다 (키와 값)
    for k in player:
        print('{0} = {1}'.format(k,player[k]))

my_abs(-1)
my_abs(2)
print('\n')
print_string('안녕하세요',3)
print('\n')
print_string2('반가워요') #count 매개변수를 입력하지 않으면 기본값으로 적용
print('\n')
print_personnel('MinGyu') #name만 지정후 나머지 변수 기본값
print('-----------------')
print_personnel('MinGyu',position='manager') #name,position 지정후 nationality 기본값
print('-----------------')
print_personnel('MinGyu',nationality='USA') #name,nationality지정후 position 기본값
print('\n')
merge_string('아버지가','방에','들어','가신다') #문자열 이어주기
print_team(카시야스='GK',호날두='FW',알론소='MF',페페='DF') #ex(key='value')