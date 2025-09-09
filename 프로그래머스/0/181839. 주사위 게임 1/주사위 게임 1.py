def solution(a, b):
    points = 0
    if a % 2 != 0 and b % 2 != 0: 
        points = a**2 + b**2
    elif (a %2 != 0 and b % 2 == 0) or (a %2 == 0 and b %2 != 0):
        points = 2 * (a + b)
    else: 
        points = abs(a - b)
        
    return points