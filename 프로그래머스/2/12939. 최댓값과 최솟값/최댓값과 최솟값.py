def solution(s):
    answer = ''
    s = list(map(int, s.split(' ')))
    mini = min(s)
    maxi = max(s)
    return str(mini) + ' ' + str(maxi)