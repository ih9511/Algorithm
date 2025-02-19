import sys

input = sys.stdin.readline

T = int(input())
# print(T, type(T))
for i in range(T):
    li = []
    char = str(input().rstrip())
    
    
    
    for ch in char:        
        if char[0] == ')':
            print('NO')
            break
    
        if len(li) == 0: li.append(ch)
        else:
            if li[-1] == '(' and ch == ')':
                li.pop()
            else:
                li.append(ch)
            
            
    if li == [] and char[0] != ')':
        print('YES')
        
    if li != [] and char[0] != ')':
        print('NO')