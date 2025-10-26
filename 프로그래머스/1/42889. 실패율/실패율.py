def solution(N, stages):
    total_users = len(stages)
    result = []
    # 각 스테이지에 멈춘 인원 수 계산
    people = [0] * (N + 2)
    for stage in stages:
        people[stage] += 1

    challenger = total_users
    for i in range(1, N + 1):
        if challenger == 0:
            fail_rate = 0
        else:
            fail_rate = people[i] / challenger
        result.append((i, fail_rate))
        challenger -= people[i]   # 다음 스테이지로 넘어갈 사람 수

    # 실패율 높은 순, 실패율 같으면 스테이지 번호 작은 것 먼저
    result.sort(key=lambda x: (-x[1], x[0]))

    return [r[0] for r in result]