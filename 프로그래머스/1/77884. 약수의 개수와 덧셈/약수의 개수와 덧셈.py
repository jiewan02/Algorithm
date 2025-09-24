def solution(left, right):
    odd = 0
    even = 0
    sum = 0
    for i in range(left, right+1): 
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count % 2 != 0: 
            sum += i
        else: 
            sum -= i
    return sum