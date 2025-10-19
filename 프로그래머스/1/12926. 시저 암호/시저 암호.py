def solution(s, n):
    result = ''
    for ch in s:
        if ch.isupper(): 
            result += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        elif ch.islower():  
            result += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        else:  
            result += ch
    return result
