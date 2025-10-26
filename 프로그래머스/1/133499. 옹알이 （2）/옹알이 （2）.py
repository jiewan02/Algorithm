def solution(babbling):
    truth = ['aya', 'ye', 'woo', 'ma']
    result = 0
    for babble in babbling: 
        temp = babble
        prev = ''
        while temp:
            matched = False
            for i in truth:
                if temp.startswith(i) and prev != i:
                    prev = i
                    temp = temp[len(i):]   # 발음 성공한 부분만큼 제거
                    matched = True
                    break
            if not matched:
                break
        if not temp:  # 모두 다 처리됐으면 성공!
            result += 1
    return result