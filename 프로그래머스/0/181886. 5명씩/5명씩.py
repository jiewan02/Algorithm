def solution(names):
    result = []
    
    for i in range(len(names)): 
        if i % 5 == 0: 
            result.append(names[i])
            
    return result