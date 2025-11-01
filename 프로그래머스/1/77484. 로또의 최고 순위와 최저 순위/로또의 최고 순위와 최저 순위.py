def solution(lottos, win_nums): 
    answer = []
    zero = 0
    match = 0
    
    for i in range(len(lottos)): 
        if sum(lottos) == 0: 
            answer = [1, 6]
            break
            
        if lottos[i] == 0: 
            zero += 1
        elif lottos[i] in win_nums: 
            match += 1
        
    if not answer: 
        best = match + zero
        worst = match
        
        def rank(x): 
            return 7-x if x >=2 else 6
        
        answer = [rank(best), rank(worst)]
        
    return answer