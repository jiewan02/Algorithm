def solution(my_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = []
    for i in alpha: 
        count = my_string.count(i)
        result.append(count)
    return result