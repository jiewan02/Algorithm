def solution(array, n):
    diff = [0] * len(array)
    for i in range(len(array)): 
        diff[i] = abs(array[i] - n)
    idx = min(diff) 
    
    candidates = []
    for i in range(len(array)):
        if diff[i] == idx:
            candidates.append(array[i])
            
    return min(candidates)
        