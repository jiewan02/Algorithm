def solution(arr, flag):
    result = []
    
    for i, n in enumerate(arr): 
        if flag[i]: 
            result += [n for j in range(n*2)]
        else:
            result = result[:len(result)-n]
            
    return result