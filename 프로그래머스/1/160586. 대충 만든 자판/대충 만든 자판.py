def solution(keymap, targets):
    answer = []
    # 1. 누름 횟수를 기록할 dict
    press_count = {}
    for keys in keymap:  
        for idx, ch in enumerate(keys):
            # 최소 횟수만 기록
            if ch not in press_count:
                press_count[ch] = idx + 1
            else:
                press_count[ch] = min(press_count[ch], idx + 1)
    
    # 2. targets별로 계산
    for target in targets:
        cnt = 0
        for t in target:
            if t in press_count:
                cnt += press_count[t]
            else:
                cnt = -1    # 못 만드는 문자
                break
        answer.append(cnt)
    
    return answer