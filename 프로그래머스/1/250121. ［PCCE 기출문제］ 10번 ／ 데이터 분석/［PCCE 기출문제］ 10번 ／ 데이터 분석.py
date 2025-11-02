def solution(data, ext, val_ext, sort_by):
    # 컬럼명과 인덱스 매칭 (문제 설명대로 순서 지정)
    col_index = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    ext_idx = col_index[ext]
    sort_idx = col_index[sort_by]

    # 1. 조건에 맞는 것만 필터링
    filtered = [row for row in data if row[ext_idx] < val_ext]

    # 2. 정렬
    sorted_data = sorted(filtered, key=lambda x: x[sort_idx])
    return sorted_data