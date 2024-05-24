def solution(survey, choices):
    answer = ''
    mbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] > 4:
            mbti[survey[i][1]] += abs(choices[i] - 4)
        
        elif choices[i] < 4:
            mbti[survey[i][0]] += abs(choices[i] - 4)
            
    
    if mbti['R'] >= mbti['T']:
        #answer.append('R')
        answer += 'R'
    elif mbti['R'] < mbti['T']:
        #answer.append('T')
        answer += 'T'
    
    if mbti['C'] >= mbti['F']:
        #answer.append('C')
        answer += 'C'
    elif mbti['C'] < mbti['F']:
        #answer.append('F')
        answer += 'F'
        
    if mbti['J'] >= mbti['M']:
        #answer.append('J')
        answer += 'J'
    elif mbti['J'] < mbti['M']:
        #answer.append('M')
        answer += 'M'
        
    if mbti['A'] >= mbti['N']:
        #answer.append('A')
        answer += 'A'
    elif mbti['A'] < mbti['N']:
        #answer.append('N')
        answer += 'N'
            
    #print(mbti['R'])
    return answer