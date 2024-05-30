from itertools import permutations

def solution(k, dungeons):
    perm = list(permutations(dungeons))
    result = []
    for p in perm:
        i = 0
        new_k = k
        for dungeon in p:
            if new_k >= 0 and dungeon[0] <= new_k:
                new_k -= dungeon[1]
                i += 1
        result.append(i)
    return max(result)