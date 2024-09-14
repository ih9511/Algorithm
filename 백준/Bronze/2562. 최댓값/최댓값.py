import sys

input = sys.stdin.readline

inputList = []

for _ in range(9):
    inputList.append(int(input().strip()))
    
maxValue = max(inputList)

for idx, val in enumerate(inputList):
    if val != maxValue:
        pass
    else:
        print(maxValue)
        print(idx + 1)