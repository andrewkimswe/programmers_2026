def solution(n, info):
    answer = [-1]
    max_diff = 0

    def dfs(idx, arrows, r_board):
        nonlocal answer, max_diff

        if idx == 11:
            if arrows > 0:
                r_board[10] += arrows
            
            r_score, a_score = 0, 0
            for i in range(11):
                if r_board[i] > info[i]:
                    r_score += (10 - i)
                elif info[i] > 0:
                    a_score += (10 - i)
            
            diff = r_score - a_score
            
            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = r_board[:]
                
                elif diff == max_diff:
                    for i in range(10, -1, -1):
                        if r_board[i] > answer[i]:
                            answer = r_board[:]
                            break
                        elif r_board[i] < answer[i]:
                            break

            if arrows > 0:
                r_board[10] -= arrows
            return

        if arrows > info[idx]:
            r_board[idx] = info[idx] + 1
            dfs(idx + 1, arrows - (info[idx] + 1), r_board)
            r_board[idx] = 0

        dfs(idx + 1, arrows, r_board)

    dfs(0, n, [0] * 11)
    
    return answer