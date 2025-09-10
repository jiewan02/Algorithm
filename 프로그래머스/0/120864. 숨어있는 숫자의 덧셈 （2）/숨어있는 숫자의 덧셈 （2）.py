def solution(my_string):
    answer = 0
    for i in my_string: 
        if i.isalpha(): 
            my_string = my_string.replace(i, ' ')
    my_string = my_string.strip().split()
    for i in my_string: 
        answer += int(i)
    return answer