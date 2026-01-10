def solution(wallpaper):
    
    min_x, min_y = 51, 51
    max_x, max_y = -1, -1

    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                min_x = min(min_x, r)
                min_y = min(min_y, c)
                max_x = max(max_x, r)
                max_y = max(max_y, c)
        
    return [min_x, min_y, max_x + 1, max_y + 1]