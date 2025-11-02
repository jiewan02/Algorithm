def solution(data, ext, val_ext, sort_by):
    col_idx = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    ext_idx = col_idx[ext]
    sort_idx = col_idx[sort_by]
    
    filtered = [i for i in data if i[ext_idx] < val_ext]
    sorted_data = sorted(filtered, key = lambda x: x[sort_idx])
    return sorted_data