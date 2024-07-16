import sys


input = sys.stdin.readline

n = int(input().strip())

x = 'long ' * (n // 4) + 'int'

print(x)
