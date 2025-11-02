def solution(schedules, timelogs, startday):
    answer = 0
    for schedule, timelog in zip(schedules, timelogs):
        t = schedule + 10 # 등록 마감 시간
        
        # 시간이 넘어가는 부분 해결
        if t % 100 >= 60:
            t += 40
            
        if startday <= 5:
            ls = timelog[:6-startday]+timelog[8-startday:]
        else:
            ls = timelog[8-startday:][:5]
        
        a = 0
        for l in ls:
            if l <= t:
                a += 1
                
        if a == 5:
            answer += 1
    
    return answer