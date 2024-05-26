def solution(phone_book):
    answer = True
    
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] = 1
    #print(hash_map)
        
    for nums in phone_book:
        arr = ''
        
        for num in nums:
            # 앞에서 부터 하나씩 넣어가면서 만약 그 앞에 일치하는 데이터가 있다면 접두어가 있다는 뜻이므로
            # arr에 하나씩 넣어가는 것.
            arr += num
            #print(arr)
            if arr in hash_map and arr != nums:
                answer = False
    
    return answer