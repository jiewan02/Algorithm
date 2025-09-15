def solution(arr, k):
    answer = []
    
    for i in range(len(arr)):
        
        if arr[i] not in answer: 
            answer.append(arr[i])
            if len(answer) == k: 
                break
    if len(answer) < k: 
        answer += [-1] *(k - len(answer)) 
        
    return answer