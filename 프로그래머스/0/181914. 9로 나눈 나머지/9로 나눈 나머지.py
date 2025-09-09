def solution(number):
    result = 0
    
    for i in number: 
        result += int(i)
        
    return result % 9