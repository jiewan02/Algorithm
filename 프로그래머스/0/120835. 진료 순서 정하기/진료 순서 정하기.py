def solution(emergency):
    sorted_list = sorted(emergency, reverse=True)
    result = []
    
    for i in emergency: 
        result.append(sorted_list.index(i)+1)
        
    return result
        