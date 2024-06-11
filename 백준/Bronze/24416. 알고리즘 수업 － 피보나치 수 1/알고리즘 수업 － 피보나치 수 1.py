import sys

input = sys.stdin.readline

li = [0] * 41
n = int(input())
recur_cnt = 1
dp_cnt = 0
ans = []


def fib_recursive(n):
    global recur_cnt

    if n == 1 or n == 2:
        return 1
    else:
        recur_cnt += 1
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_dp(n):
    global dp_cnt
    li[0] = 1
    li[1] = 1
    for i in range(3, n + 1):
        dp_cnt += 1
        li[i] = li[i - 1] + li[i - 2]
    return li[n]


fib_recursive(n)
fib_dp(n)

ans = [recur_cnt, dp_cnt]
print(*ans)
