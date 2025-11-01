def solution(s): 
    answer = 0
    same = 0
    diff = 0
    for i in s: 
        if same == diff: 
            answer += 1
            a = i
        if a == i: 
            same += 1
        else: 
            diff += 1
    return answer