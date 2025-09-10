def solution(arr, flag):
    result = []
    
    for i in range(len(flag)): 
        if flag[i]:  
            result += [arr[i]] * (arr[i] * 2)
        else: 
            for j in range(arr[i]): 
                if result: 
                    result.pop()
    return result