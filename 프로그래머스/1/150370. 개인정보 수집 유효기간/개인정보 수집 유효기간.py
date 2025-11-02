def solution(today, terms, privacies):
    # 모든 날짜는 YYYY.MM.DD 형태, 달은 28일까지
    # 날짜를 총 일수로 환산하면 계산이 쉬움 (년 * 12 * 28 + 월 * 28 + 일)
    def days(date):
        y, m, d = map(int, date.split('.'))
        return (y * 12 * 28) + (m * 28) + d

    # 약관 종류별 유효기간(달) 맵 생성
    term_dict = {k: int(v) for (k, v) in (t.split() for t in terms)}

    today_days = days(today)
    answer = []
    for idx, info in enumerate(privacies):
        date, t = info.split()
        end_days = days(date) + term_dict[t]*28 - 1  # 유효기간 끝나는 날
        if end_days < today_days:
            answer.append(idx+1)  # 번호는 1부터
    return answer