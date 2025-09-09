def solution(num_list):
    odd_result = ''
    even_result = ''
    
    for i in num_list: 
        if i % 2 != 0: 
            odd_result += str(i)
        else: 
            even_result += str(i)
            
    result = int(odd_result) + int(even_result)
    
    return result
    
    