def solution(n):
    answer = 0
    answer = list(str(n))
    answer.sort()
    answer.reverse()
    return int(''.join(answer))