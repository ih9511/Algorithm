import sys


input = sys.stdin.readline

a = int(input().strip())

for i in range(1, 10):
    print(f'{a} * {i} = {a * i}')
