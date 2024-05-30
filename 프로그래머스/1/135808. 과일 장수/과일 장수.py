def solution(k, m, score):
    answer = 0
    score.sort()
    score = score[len(score) % m :]
    # print(score)
    
    for i in range(len(score) // m):
        # print(i * m)
        # print(score[i * m])
        # print('')
        answer += score[i * m] * m
        
    return answer