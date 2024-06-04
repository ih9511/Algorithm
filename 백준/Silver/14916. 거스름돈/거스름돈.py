# dp는 bottom-up 방식으로 해야함.

import sys

input = sys.stdin.readline

'''
15원이면 5원짜리 3개
14원이면 5원짜리 2개 2원짜리 2개

y = 5x1 + 2x2, where x1 and x2 are integer
'''
n = int(input())

INF = 1e9
dp = [INF] * 100001

dp[2] = 1
# dp[3] = -1
dp[4] = 2
dp[5] = 1

for i in range(6, n + 1):
    dp[i] = min(dp[i - 2], dp[i - 5]) + 1

'''
삼항 연산자

A if (조건문) else B 
'''
print(-1 if dp[n] == INF else dp[n])