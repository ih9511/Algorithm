import sys

input = sys.stdin.readline

A, B = map(int, input().strip().split(' '))

print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)