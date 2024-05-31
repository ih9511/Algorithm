import sys

from collections import deque

input = sys.stdin.readline

n = int(input())
st_type = list(map(int, input().split(" ")))  # 수열 타입, queue면 0, stack이면 1
st = list(map(int, input().split(" ")))  # 수열

m = int(input())
st_insert = list(map(int, input().split(" ")))  # 삽입할 원소를 담고 있는 수열

new_m = deque()
answer = []

for i, j in zip(st_type, st):
    # i: 수열 타입
    # j: 원소
    # 만약 queue면 새로운 원소 insert, stack이면 원소 유지
    if i == 0:
        new_m.append(j)

for i in st_insert:
    # print("before insert =", new_m)
    new_m.appendleft(i)
    # print("after append =", new_m)
    answer.append(new_m.pop())
    # print("after insert =", new_m)
    # print('')

print(*answer)
