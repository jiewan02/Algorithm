def solution(num_list):
    result = 0
    mul = 1
    for i in num_list: 
        if len(num_list) >= 11: 
            result += i
        else: 
            mul *= i
    if result != 0:
        return result
    if mul != 0: 
        return mul