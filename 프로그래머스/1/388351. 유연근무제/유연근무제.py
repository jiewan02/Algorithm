def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        for j in range(7):
            if timelogs[i][j]>overtime(schedules[i]+10):
                if (j+startday)%7 != 0 and (j+startday)%7<6:
                    answer=answer-1
                    break
        answer+=1
    return answer
def overtime(n):    
    return n//100*100+((n%100)//60)*100+(n%100)%60