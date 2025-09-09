def solution(arr, n):
    
    if len(arr) % 2 != 0: 
        for i in range(len(arr)): 
            if i % 2 == 0: 
                arr[i] = arr[i] + n
        
    if len(arr) % 2 == 0: 
        for i in range(len(arr)): 
            if i % 2 != 0: 
                arr[i] = arr[i] + n
                
    return arr