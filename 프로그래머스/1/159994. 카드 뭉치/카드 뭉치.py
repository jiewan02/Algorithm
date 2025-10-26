def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0
    len1, len2 = len(cards1), len(cards2)
    for word in goal:
        if idx1 < len1 and cards1[idx1] == word:
            idx1 += 1
        elif idx2 < len2 and cards2[idx2] == word:
            idx2 += 1
        else:
            return "No"
    return "Yes"