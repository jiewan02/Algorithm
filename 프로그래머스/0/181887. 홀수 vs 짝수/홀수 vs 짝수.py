def solution(num_list):
    
    odd_sum = 0
    even_sum = 0
    for i in range(len(num_list)): 
        if (i+1) % 2 != 0: 
            odd_sum += num_list[i]
        else: 
            even_sum += num_list[i]
    if odd_sum > even_sum: 
        return odd_sum
    else: 
        return even_sum
