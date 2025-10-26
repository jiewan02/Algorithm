def solution(babbling):
    truth = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    for i in babbling: 
        for j in truth: 
            if j * 2 not in i: 
                i = i.replace(j, ' ')
        if len(i.strip()) == 0: 
            answer += 1
            
    return answer