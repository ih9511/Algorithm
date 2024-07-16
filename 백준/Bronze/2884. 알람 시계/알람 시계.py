import sys


input = sys.stdin.readline

hour, minute = map(int, input().strip().split(' '))

if minute >= 45:
    print(f'{hour} {minute - 45}')

else:
    if hour - 1 < 0:
        print(f'23 {minute + 15}')
    else:
        print(f'{hour - 1} {minute + 15}')