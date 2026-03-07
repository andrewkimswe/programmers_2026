from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for size in course:
        temp = []
        for order in orders:
            combis = combinations(sorted(order), size)
            temp.extend(combis)
            
        counter = Counter(temp)
        
        if len(counter) != 0 and max(counter.values()) >= 2:
            max_val = max(counter.values())
            for key, value in counter.items():
                if value == max_val:
                    answer.append(''.join(key))
    return sorted(answer)