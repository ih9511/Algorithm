import sys


input = sys.stdin.readline

n = int(input().strip())

print(n * (n + 1) // 2)