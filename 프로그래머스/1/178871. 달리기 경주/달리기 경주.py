def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}

    for name in callings:
        idx = rank[name]           # 현재 등수 인덱스
        front = players[idx - 1]   # 바로 앞 선수 이름

        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        rank[name] -= 1
        rank[front] += 1

    return players