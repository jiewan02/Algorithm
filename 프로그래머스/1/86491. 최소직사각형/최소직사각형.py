def solution(sizes):
    w = 0
    h = 0
    for size in sizes:
        long_side = max(size)
        short_side = min(size)
        w = max(w, long_side)
        h = max(h, short_side)
    return w * h