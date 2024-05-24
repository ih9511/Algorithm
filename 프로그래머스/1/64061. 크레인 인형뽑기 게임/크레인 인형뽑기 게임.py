def solution(board, moves):
    stack = [0, 0] # 인형을 뽑아서 담을 스택
    size_of_board = len(board[0]) # board의 크기
    cnt = 0 # 사라진 인형의 수
    
    for move in moves:
        
        for i in range(size_of_board):
            
            if board[i][move - 1] != 0: # 만약 move 칸에 인형이 있다면,
                
                if stack[-1] == board[i][move - 1]: # 그 인형이 stack에 채워져 있는 인형과 같다면
                    stack.pop() # 인형 없애기
                    cnt += 2 # 사라진 인형은 2개이므로 +2
                    
                else: # move 칸의 인형과 stack 최상단 인형이 다르다면,
                    stack.append(board[i][move - 1]) # stack에 해당 인형을 채우기
                    
                board[i][move - 1] = 0 # board에서 move 칸에 인형이 사라졌으므로 0 집어넣기
                
                break # break가 없다면 끝까지 순회하므로 인형을 발견했으면 for문 정지 후 다음 move로 이동
                
            # else: # 만약 move 칸에 인형이 없다면,
            #     cnt += 0 # 아무 일도 일어나지 않음
                
    return cnt