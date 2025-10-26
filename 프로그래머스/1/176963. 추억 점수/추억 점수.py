def solution(name, yearning, photo):
    dictionary = dict(zip(name, yearning))
    
    scores = []
    
    for i in photo: 
        score = 0
        for j in i: 
            if j in dictionary: 
                score += dictionary[j]
        scores.append(score)
    return scores