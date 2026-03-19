def solution(s):
    answer = len(s)
    
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        
        for j in range(step, len(s), step):
            next_step = s[j:j+step]
            
            if prev == next_step:
                count += 1
            else:
                compressed += (str(count) + prev) if count >= 2 else prev
                
                prev = next_step
                count = 1
        
        compressed += (str(count) + prev) if count >= 2 else prev
        
        answer = min(answer, len(compressed))
        
    return answer