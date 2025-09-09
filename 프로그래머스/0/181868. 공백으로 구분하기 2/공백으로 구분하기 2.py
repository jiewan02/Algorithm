def solution(my_string):
    answer = my_string.split(' ')
    result = []
    for i in answer: 
        if i.isalpha(): 
            result.append(i)
    return result