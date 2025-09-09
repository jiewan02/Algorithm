def solution(num_list):
    index = -1
    for i in num_list: 
        if i < 0: 
            index = num_list.index(i)
            break
        
    return index