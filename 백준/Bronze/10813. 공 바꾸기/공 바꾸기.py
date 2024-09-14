import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))

bucket = [i for i in range(1, N + 1)]

for _ in range(M):
    temp = 0
    i, j = map(int, input().strip().split(' '))
    temp = bucket[i - 1]
    bucket[i - 1] = bucket[j - 1]
    bucket[j - 1] = temp
    
print(*bucket)