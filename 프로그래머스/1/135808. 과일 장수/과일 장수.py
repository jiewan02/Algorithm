def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    new_list = []
    for i in range(0, len(score), m): 
        new_list.append(score[i:i+m])
    # print(new_list)  # 디버깅용

    for box in new_list:
        if len(box) == m:         # 박스가 m개일 때만 판매
            answer += min(box) * m
        # m개 미만이면 자동으로 버림

    return answer