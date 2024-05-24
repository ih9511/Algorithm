def solution(genres, plays):
    answer = []
    hash_map = {} # 장르 별 재생 횟수
    
    # hash_map 만들기
    for i in set(genres):
        hash_map[i] = 0
    # 각 장르 별 전체 재생 횟수를 hash_map에 갱신
    for i in range(len(genres)):
        hash_map[genres[i]] += plays[i]
    
    # for i in range(len(genres)):
    #     genres[i] += str(i)
    
    # hash_map을 가장 많이 재생된 장르부터 내림 차순으로 정렬
    sorted_hash_map = sorted(hash_map.items(), key = lambda x: x[1], reverse = True)
    print('sorted_hash_map:', sorted_hash_map)
    
    # genres = ['classic', 'pop', 'classic', 'classic', 'pop']
    # plays = [500, 600, 150, 800, 2500]
    # hash_map = {'pop': 3100, 'classic': 1450}
    sorted_hash_map_list = [] # 노래 순위만 가진 list 따로 정의 필요
    for i in sorted_hash_map:
        sorted_hash_map_list.append(i[0])
    print(sorted_hash_map_list)
    # genres에서 pop인 index를 찾고 같은 index의 plays 값 확인
    
    # 재생 횟수를 따라서 정렬
    # point: index를 어떻게 다시 가져올 것인가?
    index_list = []
    for i in range(len(genres)):
        index_list.append(i)
    ziplist = list(zip(genres, plays, index_list))
    ziplist.sort(key = lambda x: x[1], reverse = 1)
    print('ziplist =', ziplist)
    
    # 각 인덱스의 재생 횟수를 담은 hash 맵 추가 정의
    # 조건: 장르 별로 가장 많이 재생된 노래를 두 개씩 모음
    hash_map_song = {}
    for i in ziplist:
        hash_map_song[i[0]] = []
    for i in ziplist:
        hash_map_song[i[0]].append([i[1], i[2]])
    print(hash_map_song)
    for i in sorted_hash_map_list:
        # 모든 장르에 곡이 2개 이상 있으리라는 법이 없기 때문에...
        if len(hash_map_song.get(i)) >= 2:
            # answer.append(hash_map_song.get(i))
            # answer.append(hash_map_song.get(i))
            answer.append(hash_map_song[i][0][1])
            answer.append(hash_map_song[i][1][1])
        else:
            answer.append(hash_map_song[i][0][1])
        #print(hash_map_song[i])
        
    #print(hash_map_song)
    
    return answer