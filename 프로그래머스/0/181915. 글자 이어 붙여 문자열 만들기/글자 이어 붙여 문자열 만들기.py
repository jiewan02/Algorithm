def solution(my_string, index_list):
    answer = ''
    
    for j in index_list: 
        answer += my_string[j]
            
    return answer