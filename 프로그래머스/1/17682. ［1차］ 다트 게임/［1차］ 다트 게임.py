def solution(dartResult):
    score = []
    i = 0
    length = len(dartResult)
    while i < length:
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and i+1 < length and dartResult[i+1] == '0':
                num = 10
                i += 1  
            else:
                num = int(dartResult[i])
            i += 1
            if dartResult[i] == 'S':
                num = num ** 1
            elif dartResult[i] == 'D':
                num = num ** 2
            elif dartResult[i] == 'T':
                num = num ** 3
            if i+1 < length and dartResult[i+1] in ['*','#']:
                if dartResult[i+1] == '*':
                    num *= 2
                    if score:
                        score[-1] *= 2  
                elif dartResult[i+1] == '#':
                    num *= -1
                i += 1 
            score.append(num)
        i += 1
    return sum(score)