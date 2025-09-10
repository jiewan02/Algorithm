def solution(strArr):
    count_dict = {}
    for s in strArr:
        length = len(s)
        if length in count_dict:
            count_dict[length] += 1 
        else:
            count_dict[length] = 1  
    
    return max(count_dict.values())