def solution(t, p):
    answer = 0
    length = len(p)
    
    new_string = ''
    for i in range(len(t)): 
        new_string = t[i:i+len(p)]
        if int(new_string) <= int(p) and len(new_string) == length: 
            answer += 1
    return answer