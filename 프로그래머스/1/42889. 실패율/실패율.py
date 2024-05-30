def solution(N, stages):
    answer = []
    di = {}
    # for i in range(1, N + 1):
    #     di[i] = 0
    for i in range(1, N + 1):
        challenger = 0
        fail = 0
        for j in stages:
            if j >= i:
                challenger += 1
            if j == i:
                fail += 1
        if challenger == 0:
            di[i] = 0.0
        else:
            di[i] = fail / challenger
    di = sorted(di.items(), key = lambda x: x[1], reverse = True)
    for i in di:
        answer.append(i[0])
    return answer