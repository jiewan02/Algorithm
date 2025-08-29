def solution(letter):
    
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    
    my_string = []
    
    letter = letter.split(' ')
    print(letter)
    
    for i in letter:
        for j in morse.keys():
            if i == j:
                my_string.append(morse[i])
    
    my_string = ''.join(my_string)

                
    return my_string