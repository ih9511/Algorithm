import sys

from collections import deque

input = sys.stdin.readline

n = int(input())
row = deque()
row_info = []

for i in range(n):
    x = list(map(int, input().split(" ")))

    if x[0] == 1:
        row.append(x[1])
    else:
        try:
            row.pop()
        except:
            continue

    # print(row)

    try:
        row_info.append([len(row), row[-1]])
    except:
        continue

# print(row_info)

max_len = 0
for i in row_info:
    if i[0] > max_len:
        max_len = i[0]
        student_num = i[1]
    elif i[0] == max_len:
        student_num = min(student_num, i[1])
# print('max_len =', max_len)
# print('student_num =', student_num)

print(f"{max_len} {student_num}")
