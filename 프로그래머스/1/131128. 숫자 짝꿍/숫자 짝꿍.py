def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1): 
        countX = X.count(str(i))
        countY = Y.count(str(i))
        answer += str(i) * min(countX, countY)
        
    if answer == '': 
        return '-1'
    if set(answer) == {'0'}: 
        return '0'
    
    return answer