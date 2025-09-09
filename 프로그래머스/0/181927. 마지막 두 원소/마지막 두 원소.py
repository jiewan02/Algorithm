def solution(num_list):
    
    i = num_list[-1]
    j = num_list[-2]
    
    if i > j:
        num_list.append(i-j)
    else:
        num_list.append(i*2)
        
    return num_list