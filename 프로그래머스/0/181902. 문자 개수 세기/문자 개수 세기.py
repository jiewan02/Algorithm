def solution(my_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = []
    for i in alpha: 
        result.append(my_string.count(i))
    return result