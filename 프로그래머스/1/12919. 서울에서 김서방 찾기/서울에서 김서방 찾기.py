def solution(seoul):
    answer = ''
    idx = 0
    for i in range(len(seoul)): 
        if seoul[i] == "Kim": 
            idx = i
    
    return "김서방은 " + str(idx) + "에 있다"