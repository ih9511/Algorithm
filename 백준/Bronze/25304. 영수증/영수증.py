import sys


input = sys.stdin.readline

total_price = 0
X = int(input().strip())
N = int(input().strip())

for _ in range(N):
    a, b = map(int, input().strip().split())
    total_price += a * b
    
if total_price != X:
    print("No")
else:
    print("Yes")