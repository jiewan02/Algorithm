def solution(survey, choices):
    # 결과 담을 dict
    chars = "RTCFJMAN"
    scores = {ch: 0 for ch in chars}
    type_pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for s, c in zip(survey, choices):
        if c < 4:  # 비동의
            scores[s[0]] += 4 - c
        elif c > 4:  # 동의
            scores[s[1]] += c - 4
        # c==4는 점수 없음
    
    result = ""
    for a, b in type_pairs:
        # 더 점수 높은 쪽, 같으면 사전순
        result += a if scores[a] >= scores[b] else b
    
    return result