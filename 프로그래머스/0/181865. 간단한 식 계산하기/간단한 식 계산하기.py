def solution(binomial):
    
    new_list = binomial.split(' ')
    result = 0
    for i in new_list: 
        if i.isdigit(): 
            continue
        else: 
            if i == '+':
                result = int(new_list[0]) + int(new_list[2])
            elif i == '-':
                result = int(new_list[0]) - int(new_list[2])
            else:
                result = int(new_list[0]) * int(new_list[2])
    
    
    return result