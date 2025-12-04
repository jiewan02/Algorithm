def solution(A,B):
    answer = 0
    score = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)): 
        score += A[i] * B[i]
    return score