from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    target = {w: n for w, n in zip(want, number)}
    
    current_win = Counter(discount[:10])
    
    for i in range(len(discount) - 9):
        if current_win == target:
            answer += 1
        
        if i + 10 < len(discount):
            current_win[discount[i]] -= 1
            if current_win[discount[i]] == 0:
                del current_win[discount[i]]
            current_win[discount[i+10]] += 1
            
    return answer