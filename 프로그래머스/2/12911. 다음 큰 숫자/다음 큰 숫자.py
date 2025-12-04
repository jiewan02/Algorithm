def solution(n):
    target = bin(n).count('1')
    print(target)
    num = n + 1
    
    while True: 
        if bin(num).count('1') == target: 
            return num
        num += 1