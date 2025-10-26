def solution(n):
    real_count = 0
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            real_count += 1
    return real_count

def is_prime(n): 
    if n < 2: 
        return False
    
    for i in range(n): 
        if n % i == 0: 
            return False
    return True