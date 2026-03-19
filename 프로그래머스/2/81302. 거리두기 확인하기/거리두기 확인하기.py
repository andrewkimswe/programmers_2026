def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5:
                        if place[nr][nc] == 'P': 
                            return False
                        
                        if place[nr][nc] == 'O':
                            nnr, nnc = nr + dr, nc + dc
                            if 0 <= nnr < 5 and 0 <= nnc < 5:
                                if place[nnr][nnc] == 'P':
                                    return False

                for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == 'P':
                        if place[r][nc] != 'X' or place[nr][c] != 'X':
                            return False
    return True

def solution(places):
    answer = []
    for p in places:
        if check(p):
            answer.append(1)
        else:
            answer.append(0)
    return answer