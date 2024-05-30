from collections import defaultdict
def solution(clothes):
    answer = 1
    # hash_map = defaultdict(list)
    hash_map = {i[1]:[] for i in clothes}
    
    # 옷의 종류를 key로 하여 hash_map 구성
    # for i in clothes:
    #     hash_map[i[1]] = []
    for i in clothes:
        hash_map[i[1]].append(i[0])
    
    
    # 조합의 개수 구하기
    # 각 value list의 길이 + 1 값들을 다 곱하고 - 1
    for i in hash_map:
        answer *= len(hash_map[i]) + 1
    
    return answer - 1