def solution(n, lost, reserve):
    # 겹치는 학생을 set으로 뽑아내고, 각각에서 제거
    overlap = set(lost) & set(reserve)
    lost = [l for l in lost if l not in overlap]
    reserve = [r for r in reserve if r not in overlap]

    for r in sorted(reserve):  # 작은 번호부터 빌려주기!
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n - len(lost)