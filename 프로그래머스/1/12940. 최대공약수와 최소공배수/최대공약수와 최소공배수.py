def solution(n, m):
    answer = []
    maximum = 1
    minimum = n*m
    
    for i in range(1, max(n, m)): 
        if n % i == 0 and m % i == 0: 
            maximum = i 
        
    for i in range(n*m, max(n, m)-1, -1): 
        if i % m == 0 and i % n == 0 : 
            minimum = i
            
    return [maximum, minimum]