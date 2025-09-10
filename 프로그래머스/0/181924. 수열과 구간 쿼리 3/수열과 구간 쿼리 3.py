def solution(arr, queries):
    
    for query in queries: 
        idx1, idx2 = query[0], query[1]
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        
    return arr