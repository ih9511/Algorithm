from itertools import combinations

def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    comb = list(combinations(nums, 3))
    for i in comb:
        if isprime(sum(i)):
            answer += 1
    
    return answer