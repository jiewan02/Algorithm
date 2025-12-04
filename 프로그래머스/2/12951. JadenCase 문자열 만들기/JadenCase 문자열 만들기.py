def solution(s):
    answer = ''
    new_word = True
    
    for i in s: 
        if new_word: 
            answer += i.upper()
        else: 
            answer += i.lower()
        
        if i == ' ':
            new_word = True
        else: 
            new_word = False
            
    return answer