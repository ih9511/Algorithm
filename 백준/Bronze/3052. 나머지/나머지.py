import sys

input = sys.stdin.readline

inputList = []
modList = []

for _ in range(10):
    inputList.append(int(input().strip()))

for i in inputList:
    modList.append(i % 42)

print(len(set(modList)))