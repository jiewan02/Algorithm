def solution(x):
    ha = 0
    for i in str(x):
        ha += int(i)
        
    if x % ha == 0: 
        return True
    else:
        return False
