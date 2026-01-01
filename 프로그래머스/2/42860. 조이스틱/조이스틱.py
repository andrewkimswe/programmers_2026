def solution(name):
    up_down = 0
    n = len(name)
    min_move = n - 1
    
    for char in name:
        if ord(char) > ord('N'):
            up_down += ord('Z') - ord(char) + 1
        else:
            up_down += ord(char) - ord('A')
            
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        min_move = min(min_move, i + (n - next_idx) + min(i, n - next_idx))
        
    answer = up_down + min_move
    return answer