def solution(cards1, cards2, goal):
    p1 = p2 = 0
    
    for word in goal:
        if p1 < len(cards1) and word == cards1[p1]:
            p1 += 1
        elif p2 < len(cards2) and word == cards2[p2]:
            p2 += 1
        else:
            return "No"
            
    return "Yes"