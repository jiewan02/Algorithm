def solution(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls-share))

def factorial(n): 
    answer = 1
    for i in range(2, n+1): 
        answer *= i
    return answer