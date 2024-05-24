from collections import deque

def solution(bandage, health, attacks):
    # t초 동안 1초마다 x만큼 체력 회복
    # t초 연속으로 붕대 감는다면, y만큼 추가 회복
    # 최대 체력 존재
    # bandage = [시전 시간, 1초당 회복량, 추가 회복량]
    # health = 최대 체력
    # attacks = [공격 시간, 피해량]
    character = {'health': health, 'time': 1, 'band_time': 1}
    attacks = deque(attacks)
    i = 1
    while True:
        if character['time'] != attacks[0][0]:
            character['health'] += bandage[1]
            character['band_time'] += 1
            if character['band_time'] == bandage[0]:
                character['health'] += bandage[2]
                character['band_time'] = 0
            if character['health'] > health:
                character['health'] = health
        elif character['time'] == attacks[0][0]:
            character['health'] -= attacks[0][1]
            attacks.popleft()
            character['band_time'] = 0
            # while len(attacks) > 0 and character['time'] == attacks[0][0]:
            #     character['health'] -= attacks[0][1]
            #     attacks.popleft()
        if character['health'] <= 0:
            return -1
        if len(attacks) == 0:
            break
        character['time'] += 1
        i += 1
                
    
    return character['health']