import sys

input = sys.stdin.readline

n = int(input())

for i in range(4294967295):
    # print(i ** 2 + i - 2 * n)
    if n == 1:
        print(1)
        break

    elif i**2 + i - 2 * n > 0:
        print(i - 1)
        break
