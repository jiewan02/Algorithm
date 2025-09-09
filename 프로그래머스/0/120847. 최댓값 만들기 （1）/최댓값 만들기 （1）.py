def solution(numbers):
    
    numbers.sort() 
    
    max1, max2 = numbers[-1], numbers[-2]
    
    return max1 * max2