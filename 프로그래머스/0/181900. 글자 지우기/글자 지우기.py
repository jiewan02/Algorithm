def solution(my_string, indices):
    
    return ''.join(["" if i in indices else my_string[i] for i in range(len(my_string))])

