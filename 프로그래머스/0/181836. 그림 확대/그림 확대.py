def solution(picture, k):
    answer = []
    for i in picture: 
        an = ''
        for j in i: 
            an += j * k
        for x in range(k): 
            answer.append(an)
        
    return answer