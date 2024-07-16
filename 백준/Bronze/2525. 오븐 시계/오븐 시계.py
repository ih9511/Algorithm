import sys


input = sys.stdin.readline

hour, minute = map(int, input().strip().split(' '))
time = int(input())

hour_time, minute_time = time // 60, time % 60

print(f'{(hour + hour_time + (minute + minute_time) // 60) % 24} {(minute + minute_time) % 60}')