from collections import Counter

def solution(clothes):
    answer = 1
    
    counts = Counter([c[1] for c in clothes])
    
    for count in counts.values():
        answer *= (count+1)
        
    return answer - 1
    
    