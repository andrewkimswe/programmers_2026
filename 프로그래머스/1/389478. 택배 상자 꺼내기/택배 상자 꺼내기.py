def solution(n, w, num):
    
    def get_pos(target):
        row = (target - 1) // w
        if row % 2 == 0:
            col = (target - 1) % w
        else:
            col = (w - 1) - ((target - 1) % w)
        return row, col

    target_row, target_col = get_pos(num)
    max_row = (n - 1) // w
    answer = 0

    for r in range(target_row, max_row + 1):
        if r % 2 == 0:
            current_num = r * w + (target_col + 1)
        else:
            current_num = r * w + (w - target_col)
        
        if current_num <= n:
            answer += 1
            
    return answer