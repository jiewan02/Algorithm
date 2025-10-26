def solution(answers):
    # 1, 2, 3번 찍는 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    result = []
    
    for idx, answer in enumerate(answers): 
        if answer == p1[idx % len(p1)]:
            scores[0] += 1
        if answer == p2[idx % len(p2)]:
            scores[1] += 1
        if answer == p3[idx % len(p3)]: 
            scores[2] += 1
    
    for idx, s in enumerate(scores): 
        if s == max(scores):
            result.append(idx + 1)
            
    return result

    return result