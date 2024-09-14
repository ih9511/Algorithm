import sys

input = sys.stdin.readline

N = int(input().strip())

inputList = list(map(int, input().strip().split()))

print(min(inputList), max(inputList))