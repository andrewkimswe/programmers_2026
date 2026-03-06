def solution(m, n, board):
    b = [list(row) for row in board]
    answer = 0
    
    while True:
        matched = set()
        
        for i in range(m - 1):
            for j in range(n - 1):
                if b[i][j] != ' ' and b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1]:
                    matched.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])

        if not matched:
            break
            
        answer += len(matched)
        for i, j in matched:
            b[i][j] = ' '
            
        for j in range(n):
            top = m - 1
            for i in range(m - 1, -1, -1):
                if b[i][j] != ' ':
                    b[top][j] = b[i][j]
                    if top != i:
                        b[i][j] = ' '
                    top -= 1
                    
    return answer