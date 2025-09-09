def solution(my_string, m, c):
    result = ''
    for i in range(0, len(my_string), m): 
        result += my_string[i + c - 1]
        
    return result