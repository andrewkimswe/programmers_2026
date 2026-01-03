from collections import deque

def get_shapes(grid, target_value):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    shapes = []

    for i in range(n):
        for j in range(n):
            if grid[i][j] == target_value and not visited[i][j]:
                queue = deque([(i, j)])
                visited[i][j] = True
                current_shape = []
                
                while queue:
                    r, c = queue.popleft()
                    current_shape.append((r, c))
                
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            if not visited[nr][nc] and grid[nr][nc] == target_value:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                
                shapes.append(normalize(current_shape))
                
    return shapes

def normalize(shape):
    min_r = min(r for r, c in shape)
    min_c = min(c for r, c in shape)
    
    normalized = []
    for r, c in shape:
        normalized.append((r - min_r, c - min_c))
    
    normalized.sort()
    return normalized

def rotate(shape):
    rotated = []
    for r, c in shape:
        rotated.append((c, -r))
    
    return normalize(rotated)

def solution(game_board, table):
    blanks = get_shapes(game_board, 0)
    pieces = get_shapes(table, 1)
    
    answer = 0
    used_pieces = [False] * len(pieces)
    
    for blank in blanks:
        found = False
        for i in range(len(pieces)):
            if used_pieces[i]: continue
            
            target_piece = pieces[i]
        
            for _ in range(4):
                if blank == target_piece:
                    answer += len(blank)
                    used_pieces[i] = True
                    found = True
                    break
                
                target_piece = rotate(target_piece)
            
            if found: break
            
    return answer