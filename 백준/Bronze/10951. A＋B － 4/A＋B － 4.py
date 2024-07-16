import sys


input = sys.stdin.readline

while True:
    try:
        a, b = map(int, input().strip().split())
        print(a + b)
    except:
        break