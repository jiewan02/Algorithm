def solution(ingredient):
    answer = 0
    stack = []
    for ing in ingredient:
        stack.append(ing)
        # 햄버거 패턴 체크: stack의 마지막 4개가 [1,2,3,1]이면
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            # 4개 빼주기
            stack[-4:] = []
    return answer