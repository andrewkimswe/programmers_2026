from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    for p in permutations(dungeons, len(dungeons)):
        current_k = k
        count = 0
        
        for min_need, consume in p:
            if current_k >= min_need:
                current_k -= consume
                count += 1
            else:
                break
        
        max_dungeons = max(max_dungeons, count)
        
    return max_dungeons

# 8! = 40k 이므로 Brute Force