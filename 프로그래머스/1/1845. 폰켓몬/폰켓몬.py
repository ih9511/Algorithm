from itertools import combinations

def solution(nums):
#     nums_len = len(nums)
#     nums_set = list(set(nums))
#     nums_combinations = []
#     # print(nums_set, nums_len / 2)
#     # print('')
    
#     for i in range(int(nums_len / 2)):
#         nums_combinations.append(list(combinations(nums_set, i + 1)))
#         if list(combinations(nums_set, i + 1)) == []:
#             nums_combinations.pop()
    
#     # if len(nums_combinations[-1]) != 0:
#     #     answer = len(nums_combinations[-1])
#     # print(nums_combinations, len(nums_combinations[-1][0]))

    
    if len(nums) / 2 <= len(set(nums)):
        return len(nums) / 2
    else:
        return len(set(nums))