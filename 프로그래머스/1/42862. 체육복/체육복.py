def solution(n, lost, reserve):
    overlap = set(lost) & set(reserve)
    lost = [i for i in lost if i not in overlap]
    reserve = [i for i in reserve if i not in overlap]
    
    for i in sorted(reserve): 
        if i-1 in lost: 
            lost.remove(i-1)
        elif i+1 in lost: 
            lost.remove(i+1)
        
    return n - len(lost)