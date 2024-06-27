# https://www.acmicpc.net/problem/2178

import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

board = []
for _ in range(N):
    board.append(list(input()))
    
visited = [[False] * M for _ in range(N)]
ans = [[0] * M for _ in range(N)]

queue = deque()
queue.append((0, 0))
visited[0][0] = True
ans[0][0] = 1

while queue:
    x, y = queue.popleft()
    
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        # 0이면 이동 불가
        if board[nx][ny] =='0':
            continue
        # 만약 다음에 이동하고자 하는 칸이 방문되지 않은 칸이라면,
        if not visited[nx][ny]:
            visited[nx][ny] = True
            # 다음에 방문하는 칸은 이전에 방문한 칸보다 딱 한 칸만 더 이동하면 됨
            ans[nx][ny] = ans[x][y] + 1
            queue.append([nx, ny])
            
print(ans[N - 1][M - 1])