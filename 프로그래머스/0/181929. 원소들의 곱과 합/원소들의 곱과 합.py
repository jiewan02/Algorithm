def solution(num_list):
    sum = 0
    m = 1
    
    for i in num_list: 
        sum += i
        m *= i
        
    if m < sum**2:
        return 1
    else: 
        return 0