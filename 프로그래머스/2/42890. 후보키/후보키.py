from itertools import combinations

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    
    all_cases = []
    for i in range(1, col_len + 1):
        all_cases.extend(combinations(range(col_len), i))
    
    unique_cases = []
    for case in all_cases:
        tmp = [tuple(item[c] for c in case) for item in relation]
        if len(set(tmp)) == row_len:
            unique_cases.append(case)
        
    candidate_keys = set()
    for case in unique_cases:
        for key in candidate_keys:
            if set(key).issubset(set(case)):
                break
        else:
            candidate_keys.add(case)
            
    return len(candidate_keys)