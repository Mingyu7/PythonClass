lines = ['안녕하세요\n','Hello\n','こんにちは\n','你好。\n']

with open('All hello_utf8.txt','w',encoding='utf-8') as file: #encoding = utf-8 형식으로 저장
    file.writelines(lines)

with open('All hello_utf8.txt','r',encoding='utf-8') as file:
    lines1 = file.readlines()
    line = ''
    for line in lines1:
        print(line,end='')