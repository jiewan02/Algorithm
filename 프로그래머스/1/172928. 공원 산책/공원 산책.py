def solution(park, routes):
    y, x = [(i, j) for i, row in enumerate(park) for j, v in enumerate(row) if v == 'S'][0]
    d = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    H, W = len(park), len(park[0])
    for route in routes:
        dir, n = route.split()
        dy, dx = d[dir]
        n = int(n)
        tmp = [(y + dy*k, x + dx*k) for k in range(1, n+1)]
        if all(0 <= ny < H and 0 <= nx < W and park[ny][nx] != 'X' for ny, nx in tmp):
            y, x = tmp[-1]
    return [y, x]