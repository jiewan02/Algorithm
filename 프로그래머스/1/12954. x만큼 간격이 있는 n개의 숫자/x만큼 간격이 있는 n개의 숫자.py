def solution(x, n):
    answer = []
    idx = x
    for i in range(n): 
        answer.append(x)
        x += idx
    return answer