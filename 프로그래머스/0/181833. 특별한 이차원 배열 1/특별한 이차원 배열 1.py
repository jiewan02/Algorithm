def solution(n):
    answer = []
    
    for i in range(n):
        new_row = []
        for j in range(n): 
            if i == j: 
                new_row.append(1)
            else: 
                new_row.append(0)
        answer.append(new_row)
    return answer