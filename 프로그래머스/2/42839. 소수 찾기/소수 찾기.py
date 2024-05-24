from itertools import permutations
import math

# 소수 여부에 따라 boolean 반환(소수면 True, 아니면 False)
def prime_number(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = [] # input을 하나씩 분리해서 담아놓는 리스트
    for i in numbers:
        num_list.append(i)
        
    perm_list = [] # 모든 카드들을 활용한 순열을 담은 리스트
    for i in range(len(num_list)):
        perm_list += list(permutations(num_list, i + 1))
    # print('perm_list = ', perm_list)
    
    # 순열을 순회하면서 
    number_list = [] # 순열을 담아놓을 리스트
    for perm in perm_list:
        number_list.append(int("".join(perm)))
    number_list = set(number_list)
        
    for i in number_list:
        if prime_number(int(i)):
            answer += 1
    
    return answer