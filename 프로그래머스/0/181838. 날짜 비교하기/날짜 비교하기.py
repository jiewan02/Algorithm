def solution(date1, date2):
    answer = 0
    year, month, day = date1
    
    if year < date2[0]:
        answer = 1
    if year == date2[0] and month < date2[1]:
        answer = 1
    if year == date2[0] and month == date2[1] and day < date2[2]:
        answer = 1
    return answer