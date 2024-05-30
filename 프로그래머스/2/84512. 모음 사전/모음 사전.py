from itertools import product

def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    li1 = []
    li2 = []

    for i in range(5):
        li1 += product(alpha, repeat = i + 1)
    for i in li1:
        li2.append(''.join(list(i)))
    li2.sort()
    
    # for i, j in enumerate(li2):
    #     if j == word:
    #         return i + 1
        
    return li2.index(word) + 1