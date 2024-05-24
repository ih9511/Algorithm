def solution(data, ext, val_ext, sort_by):
    answer = []
    mapping_dict = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    # ext를 기준으로 val_ext 보다 큰 ext를 가지는 데이터 삭제
    for element in data:
        if element[mapping_dict[ext]] < val_ext:
            # val_ext보다 작은 element는 answer에 넣기
            answer.append(element)
    #print(answer)
    
    # i는 무엇을 기준으로 (code, date, maximum, remain) data를 정렬할 것인지(sort_by)
    answer = sorted(answer, key = lambda dataset: dataset[mapping_dict[sort_by]])
    
    return answer