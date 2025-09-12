def solution(arr, queries):
    answer = []
    for s, e, k in queries: 
        min_val = -1
        for i in range(s, e+1):
            if arr[i] > k: 
                if min_val == -1 or arr[i] < min_val:
                    min_val = arr[i]
        answer.append(min_val)
    return answer