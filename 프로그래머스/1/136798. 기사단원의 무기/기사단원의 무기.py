def solution(number, limit, power):
    answer = 0
    yaksu_list = []
    
    for i in range(1, number+1): 
        yaksu = 0
        for j in range(1, int(i**0.5)+1): 
            if i % j == 0: 
                if j == i // j:
                    yaksu += 1      
                else:
                    yaksu += 2      
        yaksu_list.append(yaksu)
        
    for i in yaksu_list: 
        if i > limit: 
            i = power
        answer += i
    return answer