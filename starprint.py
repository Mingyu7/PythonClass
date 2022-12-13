print("별출력")
for i in range(0,5,1):
    print('{:<5}'.format("*"*(i+1))) #별을 반복횟수만큼 곱해서 출력
print('\n')
for j in range(6,0,-1):
    print('{:<5}'.format('*'*(j-1)))
print('\n')
for i in range(6,0,-1):
    print('{:>5}'.format('*'*(i-1)))
print('\n')
for i in range(0,5,1):
    print('{:>5}'.format('*'*(i+1)))
print('\n')
for i in range(1,11,2): #2씩 증가 피라미드
    print('{:^10}'.format('*'*i))
print('\n')
for i in range(1,11,2): 
    print('{:^10}'.format('*'*i))
for i in range(9,0,-2):
    print('{:^10}'.format('*'*i))
print('\n')
for i in range(9,0,-2):
    print('{:^10}'.format('*'*i))
for i in range(1,11,2):
    print('{:^10}'.format('*'*i))
