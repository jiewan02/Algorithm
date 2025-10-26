def solution(answers):
    # 1, 2, 3번 찍는 패턴
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 점수 계산
    scores = [
        sum([answers[i] == p1[i % len(p1)] for i in range(len(answers))]),
        sum([answers[i] == p2[i % len(p2)] for i in range(len(answers))]),
        sum([answers[i] == p3[i % len(p3)] for i in range(len(answers))])
    ]
    max_score = max(scores)
    # 1~3번 중 공동 1등만 result에 담음
    result = [i+1 for i, score in enumerate(scores) if score == max_score]

    return result