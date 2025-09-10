def solution(myString, pat):
    count = 0
    i = 0
    while i <= len(myString) - len(pat):
        if myString[i:i + len(pat)] == pat:
            count += 1
        i += 1
    return count