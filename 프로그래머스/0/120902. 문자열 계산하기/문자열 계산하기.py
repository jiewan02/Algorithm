def solution(my_string):
    
    my_string = my_string.split()
    answer = int(my_string[0])
    
    for i in range(1, len(my_string), 2): 
        if not my_string[i].isdigit():
            if my_string[i] == '+': 
                answer += int(my_string[i+1])
                i += 1
            else: 
                answer -= int(my_string[i+1])
                i += 1
                
    return answer
            
