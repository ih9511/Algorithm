import sys


input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    print(' ' * (n - (i + 1)) + '*' * (i + 1))