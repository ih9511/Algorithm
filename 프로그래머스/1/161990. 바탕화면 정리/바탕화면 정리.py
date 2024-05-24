def solution(wallpaper):
    answer = [100, 100, 0, 0] #lux, luy, rdx, rdy
    loc = []
    # #의 좌표 값을 담는 리스트 구성. (loc)
    # lux = x 좌표 최소 값
    # luy = y 좌표 최소 값
    # rdx = x 좌표 최대 값 + 1
    # rdy = y 좌표 최대 값 + 1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                loc.append([i, j])
                
    for i in range(len(loc)):
        # lux
        if loc[i][0] < answer[0]:
            answer[0] = loc[i][0]
            
        # luy
        if loc[i][1] < answer[1]:
            answer[1] = loc[i][1]

        # rdx
        if loc[i][0] > answer[2] - 1:
            answer[2] = loc[i][0] + 1
            
        # rdy
        if loc[i][1] > answer[3] - 1:
            answer[3] = loc[i][1] + 1
        
        #print(loc[i], answer)
        
    return answer