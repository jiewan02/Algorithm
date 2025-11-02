def solution(survey, choices):
    # 각 지표별 유형 쌍
    indicators = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    # 점수 집계 dict 초기화
    score = {ch: 0 for ch in "RTCFJMAN"}

    for q, c in zip(survey, choices):
        disagree, agree = q[0], q[1]
        if c < 4:  # 비동의 쪽
            score[disagree] += 4 - c
        elif c > 4:  # 동의 쪽
            score[agree] += c - 4
        # c == 4이면 점수 없음

    # 결과 유형
    result = ""
    for left, right in indicators:
        if score[left] > score[right]:
            result += left
        elif score[left] < score[right]:
            result += right
        else:
            # 점수 같으면 사전순
            result += min(left, right)
    return result