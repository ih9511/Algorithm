import sys

input = sys.stdin.readline


a = int(input().strip())
b = input().strip()

print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))