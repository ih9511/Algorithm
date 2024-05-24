def dis(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def change_num(numbers):
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
        elif numbers[i] == '*':
            numbers[i] = 10
        elif numbers[i] == '#':
            numbers[i] = 12
            
    return numbers

def solution(numbers, hand):
    l_finger_loc = [3, 0] # 왼손 엄지 초기 위치 (*)
    r_finger_loc = [3, 2] # 오른손 엄지 초기 위치 (#)
    answer = ''
    
    numbers = change_num(numbers)
    
    for number in numbers:            
        if number in [1, 4, 7]:
            answer += 'L'
            l_finger_loc = [number // 3, 0]
            
        elif number in [3, 6, 9]:
            answer += 'R'
            r_finger_loc = [number // 3 - 1, 2]
            
        else: # 2, 5, 8, 0
            # 만약 왼손 엄지가 더 가깝다면
            if dis(l_finger_loc, [number // 3, 1]) < dis(r_finger_loc, [number // 3, 1]):
                answer += 'L'
                l_finger_loc = [number // 3, 1]
                
            # 만약 오른손 엄지가 더 가깝다면
            elif dis(r_finger_loc, [number // 3, 1]) < dis(l_finger_loc, [number // 3, 1]):
                answer += 'R'
                r_finger_loc = [number // 3, 1]
                
            # 만약 두 거리가 동일하다면
            else:
                # 왼손잡이면
                if hand == 'left':
                    answer += 'L'
                    l_finger_loc = [number // 3, 1]
                # 오른손 잡이면
                else:
                    answer += 'R'
                    r_finger_loc = [number // 3, 1]
            
    return answer