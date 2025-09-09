def solution(num_list, n):
    result = []
    
    result.extend(num_list[n:])
    
    result.extend(num_list[:n])
        
    return result
    