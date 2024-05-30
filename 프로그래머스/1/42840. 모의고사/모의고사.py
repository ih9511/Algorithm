def solution(answers):
    answer = []
    sp1 = [1, 2, 3, 4, 5] * 2000
    sp2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    sp3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    sp1_o, sp2_o, sp3_o = 0, 0, 0
    
    for i in range(len(answers)):
        if sp1[i] == answers[i]:
            sp1_o += 1
        if sp2[i] == answers[i]:
            sp2_o += 1
        if sp3[i] == answers[i]:
            sp3_o += 1
    
    sp_o = list(zip([1, 2, 3], [sp1_o, sp2_o, sp3_o]))
    sp_o = sorted(sp_o, key = lambda x:x[1], reverse = True)
    #print(sp_o)
    
    answer.append(sp_o[0][0])
    if sp_o[0][1] == sp_o[1][1]:
        answer.append(sp_o[1][0])
    if sp_o[0][1] == sp_o[2][1]:
        answer.append(sp_o[2][0])
            
    return answer