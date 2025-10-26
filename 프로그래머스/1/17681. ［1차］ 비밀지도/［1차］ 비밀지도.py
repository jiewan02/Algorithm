def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        row = arr1[i] | arr2[i]
        bin_row = bin(row)[2:].zfill(n)
        map_row = bin_row.replace('1', '#').replace('0', ' ')
        result.append(map_row)
    return result