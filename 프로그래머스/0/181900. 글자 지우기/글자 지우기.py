def solution(my_string, indices):
    result = ''
    
    for idx, s in enumerate(my_string): 
        if idx not in indices: 
            result += my_string[idx]
    
    return result

