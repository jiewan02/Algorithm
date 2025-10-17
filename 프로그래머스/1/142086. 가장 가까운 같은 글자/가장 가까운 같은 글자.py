def solution(s):
    answer = []
    last_seen = {}  # 각 문자의 마지막 인덱스를 저장할 딕셔너리
    
    for idx, letter in enumerate(s): 
        if letter not in last_seen: 
            answer.append(-1)  # 같은 글자가 없으면 -1 추가
        else:
            answer.append(idx - last_seen[letter])  # 이전 위치와의 차이 계산
        
        last_seen[letter] = idx  # 현재 인덱스를 마지막으로 본 인덱스로 업데이트

    return answer