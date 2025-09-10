def solution(i, j, k):
    count = 0
    for num in range(i, j+1): 
        for x in str(num): 
            if str(k) == str(x):
                count += 1
    return count