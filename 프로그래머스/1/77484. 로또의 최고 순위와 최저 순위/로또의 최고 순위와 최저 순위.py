def solution(lottos, win_nums): 
    rank = [6, 6, 5, 4, 3, 2, 1]
    count = lottos.count(0)
    answer = 0
    
    for i in win_nums: 
        if i in lottos: 
            answer += 1
    return rank[count + answer], rank[answer]