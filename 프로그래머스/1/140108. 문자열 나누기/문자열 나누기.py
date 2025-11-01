def solution(s):
    answer = 0
    i = 0

    while i < len(s):
        first = s[i]
        same = 0
        diff = 0

        for j in range(i, len(s)):
            if s[j] == first:
                same += 1
            else:
                diff += 1
            if same == diff:
                answer += 1
                i = j + 1
                break
        else:
            answer += 1
            break

    return answer