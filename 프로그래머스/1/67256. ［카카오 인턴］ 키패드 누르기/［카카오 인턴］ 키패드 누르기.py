def solution(numbers, hand):
    # 키패드 좌표 (숫자: (row, col))
    pad = {1:(0,0), 2:(0,1), 3:(0,2),
           4:(1,0), 5:(1,1), 6:(1,2),
           7:(2,0), 8:(2,1), 9:(2,2),
           '*':(3,0), 0:(3,1), '#':(3,2)}

    left = pad['*']
    right = pad['#']
    result = ''
    for num in numbers:
        if num in [1, 4, 7]:
            result += 'L'
            left = pad[num]
        elif num in [3, 6, 9]:
            result += 'R'
            right = pad[num]
        else:
            # 가운데 열(2,5,8,0)은 거리 비교
            l_dist = abs(left[0] - pad[num][0]) + abs(left[1] - pad[num][1])
            r_dist = abs(right[0] - pad[num][0]) + abs(right[1] - pad[num][1])
            if l_dist < r_dist:
                result += 'L'
                left = pad[num]
            elif r_dist < l_dist:
                result += 'R'
                right = pad[num]
            else:
                if hand == 'right':
                    result += 'R'
                    right = pad[num]
                else:
                    result += 'L'
                    left = pad[num]
    return result