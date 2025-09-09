def solution(myString, pat):
    converted = ''
    for i in myString: 
        if i == 'A':
            converted += 'B'
        else:
            converted += 'A'
            
    if pat in converted: 
        result = 1
    else: 
        result = 0
        
    return result