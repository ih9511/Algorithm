import sys

input = sys.stdin.readline
# print("a")
i = 1
while True:
    # print("b")
    lpv = list(map(int, input().split(" ")))
    if lpv == [0, 0, 0]:
        # print("c")
        break

    # l: 사용 가능 기간
    # p: 연속 일수
    # v: 총 휴가 일수

    # 만약 연속하는 P일이 모두 소진됐는데 남은 일 수가 l 보다 큰 경우
    # ex) 5 8 23, 남은 일 수 = 7일, l = 5일, 이 때는 최대 5일까지만 쓸 수 있기 때문에 lpv[0]을 더해줌.
    if lpv[2] % lpv[1] > lpv[0]:
        total = (lpv[2] // lpv[1]) * lpv[0] + lpv[0]

    # 그렇지 않은 경우
    # ex) 5 8 20, 남은 일 수 = 4일, l = 5일, 이 때는 4일을 다 쓸 수 있기 때문에 나눈 나머지를 더해줌.
    else:
        total = (lpv[2] // lpv[1]) * lpv[0] + (lpv[2] % lpv[1])
    print(f"Case {i}: {total}")
    i += 1
