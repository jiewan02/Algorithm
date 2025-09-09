def solution(a, b, c):
    score = 0
    if a == b and b == c: 
        score = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a != b and b != c and a != c: 
        score = a + b + c
    else: 
        score = (a+b+c) * (a**2 + b**2 + c**2)
        
    return score