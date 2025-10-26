def solution(n, m, section):
    answer = 0
    idx = 0
    length = len(section)
    while idx < length:
        coverage = section[idx] + m - 1
        answer += 1
        while idx < length and section[idx] <= coverage:
            idx += 1
    return answer