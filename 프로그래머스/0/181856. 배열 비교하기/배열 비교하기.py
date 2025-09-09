def solution(arr1, arr2):
    
    if len(arr1) > len(arr2): 
        return 1
    elif len(arr2) > len(arr1): 
        return -1
    else: 
        sum1 = 0
        sum2 = 0
        for i in arr1:
            sum1 += i
        for j in arr2:
            sum2 += j
        if sum1 > sum2: 
            return 1
        elif sum2 > sum1:
            return -1
        else:
            return 0