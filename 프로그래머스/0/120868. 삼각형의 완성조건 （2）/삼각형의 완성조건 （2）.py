def solution(sides):
    answer = 0
    max_side = max(sides[0], sides[1])
    min_side = min(sides[0], sides[1])
    
    return (max_side + min_side - 1) - abs(max_side - min_side)