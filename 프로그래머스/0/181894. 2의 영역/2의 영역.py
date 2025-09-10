def solution(arr):
    result = []
    new_result = []
    idx = -1
    for i in range(len(arr)): 
        if arr[i] == 2:
            result.append(i)  
            
    if not result:
        return [-1]
    if len(result) == 1: 
        return [arr[result[0]]]
    else: 
        return arr[result[0]: result[-1]+1]
    
