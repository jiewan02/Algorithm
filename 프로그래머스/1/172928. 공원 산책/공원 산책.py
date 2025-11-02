def solution(park, routes):
    H, W = len(park), len(park[0])
    # 시작점 찾기
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                y, x = i, j

    # 방향 dictionary
    d = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}

    for route in routes:
        op, n = route.split()
        dy, dx = d[op]
        n = int(n)
        ny, nx = y + dy * n, x + dx * n

        # 먼저 목적지 벗어나는지 체크
        if not (0 <= ny < H and 0 <= nx < W):
            continue

        # 이동할 경로에 장애물이 있는지 체크
        ok = True
        for k in range(1, n+1):
            cy, cx = y + dy * k, x + dx * k
            if park[cy][cx] == 'X':
                ok = False
                break
        if ok:
            y, x = ny, nx

    return [y, x]