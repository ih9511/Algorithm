from collections import deque

def solution(queue1, queue2):
    answer = 0
    k = 1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total_queue = queue1 + queue2
    limit = len(total_queue) * 3
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = sum1 + sum2
    
    if total_sum % 2 == 1 or sorted(total_queue)[-1] > total_sum // 2:
        answer = -1
        return answer
    
    # 시간 초과 예방(반복문 안에서 함수 호출 안하기 위해)
    # sum1 = sum(queue1)
    # sum2 = sum(queue2)
    
    while sum1 != sum2:
        if sum1 > total_sum // 2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
            answer += 1
            k += 1
        elif sum2 > total_sum // 2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
            answer += 1
            k += 1
        if k > limit:
            return -1
    
    return answer