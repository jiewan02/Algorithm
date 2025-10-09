def solution(s):
    new_list = s.split(' ')
    result = []
    
    for i in new_list: 
        new_word = ''
        for idx, char in enumerate(i): 
            if idx % 2 != 0: 
                new_word += char.lower()
            else: 
                new_word += char.upper()
        result.append(new_word)
    
    return ' '.join(result)