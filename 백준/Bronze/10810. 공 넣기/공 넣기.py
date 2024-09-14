import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))
buckets = {}

for i in range(N):
    buckets[i + 1] = [0]
    
for _ in range(M):
    bucketFrom, bucketTo, ballNumber = map(int, input().strip().split(' '))
    
    for i in range(bucketFrom, bucketTo + 1):
        buckets[i].append(ballNumber)

lastBall = []

for bucket in buckets:
    lastBall.append(buckets[bucket][-1])
    
print(*lastBall)