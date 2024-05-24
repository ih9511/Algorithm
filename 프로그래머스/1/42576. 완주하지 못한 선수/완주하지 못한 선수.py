def solution1(participant, completion):
    answer = ''
    part_hash = {}
    
    for i in participant:
        part_hash[i] = 0
        # part_hash[i] += 1 이 부분은 왜 dict 내부 값 변화가 없는거지
    for i in participant:
        part_hash[i] += 1
    
    for i in completion:
        part_hash[i] -= 1
    
    for i in part_hash:
        if part_hash[i] == 1:
            answer = i
    
    return answer

# Counter 사용
from collections import Counter

def solution2(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    # a = list(dict(part - comp).keys())[0]
    return list((part - comp).keys())[0]
    
        
# Counter 미사용, Dictionary 사용
from collections import defaultdict
def solution3(participant, completion):
    hash_p = {}
    ddict = defaultdict(int)
    print(ddict, type(ddict))
    for p in participant:
        hash_p[p] = hash_p.get(p, 0) + 1
        ddict[p] += 1
        # if p in hash_p:
        #     hash_p[p] += 1
        # else:
        #     hash_p[p] = 1
    print(hash_p)
    print(ddict)
    for c in completion:
        hash_p[c] -= 1
    hash_p = sorted(hash_p.items(), key = lambda x: x[1], reverse = True)
    return hash_p[0][0]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]