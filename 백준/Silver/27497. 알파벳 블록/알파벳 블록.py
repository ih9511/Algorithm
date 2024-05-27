from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

dq = deque()
last = []
for _ in range(n):
    order = input()
    order = order[: -1]
    if len(order) == 3:
        type, block = order[0], order[-1]
        if type == '1':
            dq.append(block)
            last .append('right')
        else:
            dq.appendleft(block)
            last.append('left')
    else:
        if not last:
            continue
        elif last[-1] == 'right':
            dq.pop()
            last.pop()
        else:
            dq.popleft()
            last.pop()

if dq:
    print(''.join(dq))
else:
    print('0')