def solution(arr, delete_list):

    new_list = []
    
    for x in arr: 
        if x not in delete_list: 
            new_list.append(x)
            
    return new_list
            
