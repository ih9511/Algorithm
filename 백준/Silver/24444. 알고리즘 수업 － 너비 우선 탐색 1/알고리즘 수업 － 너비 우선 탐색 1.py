import sys

from collections import deque

input = sys.stdin.readline

# N: node 개수
# M: edge 개수
# R: 시작 node
N, M, R = map(int, input().strip().split())
# visited initialize
# visited는 node 개수 + 1 개의 False로 이루어진 리스트로 초기화
visited = [False] * (N + 1)
# 얕은 복사를 방지하기 위해 * 연산자를 사용하지 않고 선언해야 함.
graph = [[] for _ in range(N + 1)]

# edge 정보 저장
for _ in range(M):
     u, v = map(int, input().strip().split())
     graph[u].append(v)
     graph[v].append(u)
     
# 오름 차순을 보장하기 위해 sort 처리
for i in range(1, N + 1):
    graph[i].sort()
     
queue = deque()
queue.append(R)
visited[R] = True

# 방문 순서를 표시해주기 위한 리스트
# cnt += 1을 통해 순서를 파악하게 됨
ans = [0] * (N + 1)
ans[R] = 1
cnt = 1 # 방문 순서

while queue: # queue 즉, 다 순회할 때 까지
    v = queue.popleft()
    # 하나의 node에 연결된 node들을 돌면서
    for w in graph[v]:
        if not visited[w]: # w가 방문되지 않았다면,
            visited[w] = True # w를 방문했다고 표시
            cnt += 1
            ans[w] = cnt
            queue.append(w)
            
for i in range(1, N + 1):
    print(ans[i])