def solution(s):
    
    count = 0
    removed = 0
    
    while s != '1': 
        
        zeros = s.count('0')
        removed += zeros
        
        s = s.replace('0', '')
        
        length = len(s)
        s = bin(length)[2:]
        
        count += 1
        
    return [count, removed]