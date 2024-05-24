import heapq

def solution(scoville, K):
    cnt = 0
    new_scoville = 0
    heapq.heapify(scoville)
    
    #heapq.heapify(scoville)
    #min_scoville = scoville
    #max_scoville = []
    #tmp = []
    #for i in scoville:
    #    heapq.heappush(tmp, (-i, i))
    #while tmp:
    #    max_scoville.append(heapq.heappop(tmp)[1])
    while scoville[0] < K:
        if len(scoville) >= 2:
            least = heapq.heappop(scoville)
            least1 = heapq.heappop(scoville)
            #print(scoville)
            new_scoville = least + least1 * 2
            #print(scoville)
            heapq.heappush(scoville, new_scoville)
            #print('last scoville :', scoville)
            cnt += 1
        elif len(scoville) == 1:
            return -1
    # 2 3 5 7 25
    return cnt