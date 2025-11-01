def solution(s, skip, index):
    answer = ''  
    for c in s:
        move = 0  
        ch = c    
        while move < index:
            ch = chr(ord(ch) + 1)
            if ch > 'z':
                ch = 'a'
            if ch in skip:
                continue
            move += 1
        answer += ch 

    return answer