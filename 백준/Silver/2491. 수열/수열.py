import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split(" ")))
count = []


def asc(asc_list):
    # li 순회하면서 커지는 수열 길이 세는 함수
    a = asc_list[0]
    cnt = 1
    for i in asc_list[1:]:
        if i >= a:
            cnt += 1
            a = i
        else:
            count.append(cnt)
            a = i
            cnt = 1
        count.append(cnt)


def des(dec_list):
    # li 순회하면서 작아지는 수열 길이 세는 함수
    d = dec_list[0]
    cnt = 1
    for i in dec_list[1:]:
        if i <= d:
            cnt += 1
            d = i
        else:
            count.append(cnt)
            d = i
            cnt = 1
        count.append(cnt)


asc(li)
des(li)

if n == 1:
    print(1)
else:
    print(max(count))
