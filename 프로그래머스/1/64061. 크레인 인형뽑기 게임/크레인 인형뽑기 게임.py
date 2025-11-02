def solution(board, moves):
    basket = []
    answer = 0
    n = len(board)
    
    for move in moves:
        col = move - 1  # 0-based index
        for row in range(n):  # 위->아래로 순회
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0  # 인형 뽑아서 빈 칸으로
                # 바구니 터지기 처리
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2  # 2개 터짐
                else:
                    basket.append(doll)
                break
    return answer