def solution(myStr):
    answer = []
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    myStr = myStr.strip()
    myStr = myStr.split()
    if not myStr: 
        return ['EMPTY']
    return myStr