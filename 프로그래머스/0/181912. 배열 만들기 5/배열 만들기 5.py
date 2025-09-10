def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs: 
        result = i[s:s+l]
        if int(result) > k: 
            answer.append(int(result))
    return answer