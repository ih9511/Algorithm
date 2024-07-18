import sys


input = sys.stdin.readline

N = int(input().strip())
li = list(map(int, input().strip().split(' ')))
v = int(input().strip())

cnt = 0
for i in li:
    if i == v:
        cnt += 1

print(cnt)