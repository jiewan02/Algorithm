def solution(N, stages): 
    result = {}
    denom = len(stages)
    
    for stage in range(1, N+1): 
        if denom != 0: 
            count = stages.count(stage)
            result[stage] = count / denom 
            denom -= count
        else: 
            result[stage] = 0
            
    return sorted(result, key = lambda x: result[x], reverse=True)