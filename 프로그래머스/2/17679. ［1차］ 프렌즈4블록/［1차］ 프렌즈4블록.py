def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        target = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '0' and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    target.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
        
        if not target:
            break
            
        answer += len(target)
        for i, j in target:
            board[i][j] = '0'
            
        for j in range(n):
            temp = [board[i][j] for i in range(m) if board[i][j] != '0']
            new_col = ['0'] * (m - len(temp)) + temp
            for i in range(m):
                board[i][j] = new_col[i]
                
    return answer