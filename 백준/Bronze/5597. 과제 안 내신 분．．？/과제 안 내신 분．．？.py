import sys

input = sys.stdin.readline
totalAttendance = set([i for i in range(1, 31)])
attendance = []

for _ in range(28):
    attendance.append(int(input().strip()))

attendance = set(attendance)
totalAttendance = sorted(list(totalAttendance - attendance))

for i in totalAttendance:
    print(i)