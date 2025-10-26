def solution(a, b):
    days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    # 1월 1일이 FRI이므로, 기준부터 며칠 지났는지 계산
    days = sum(days_in_month[:a-1]) + (b-1)
    # 기준일 2016-01-01 FRI → index 5
    return week[(5 + days) % 7]