from collections import deque

N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(input())

visited = [[-1] * M for _ in range(N)]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        
        if board[nx][ny] == '0':
            continue
        
        if visited[nx][ny] != -1:
            continue
        
        visited[nx][ny] = visited[x][y] + 1
        queue.append((nx, ny))
        
print(visited[N - 1][M - 1])