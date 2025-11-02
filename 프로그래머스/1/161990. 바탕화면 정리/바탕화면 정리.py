def solution(wallpaper):
    rows = len(wallpaper)
    cols = len(wallpaper[0])

    # 파일 좌표 모두 모으기
    points = [(i, j)
              for i in range(rows)
              for j in range(cols)
              if wallpaper[i][j] == "#"]

    # 각 축에서 min, max
    min_row = min(p[0] for p in points)
    min_col = min(p[1] for p in points)
    max_row = max(p[0] for p in points)
    max_col = max(p[1] for p in points)

    # 끝점은 max+1 (격자점이므로)
    return [min_row, min_col, max_row+1, max_col+1]