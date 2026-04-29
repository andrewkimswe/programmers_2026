from collections import Counter

def solution(clothes):
    kind_count = Counter(kind for name, kind in clothes)

    answer = 1
    for cnt in kind_count.values():
        answer *= (cnt + 1)
    
    return answer - 1