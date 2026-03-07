from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    total_sum = s1 + s2
    
    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    limit = len(q1) * 4
    answer = 0
    
    while s1 != target:
        if answer > limit:
            return -1
        
        if s1 > target:
            val = q1.popleft()
            s1 -= val
            q2.append(val)
        else:
            val = q2.popleft()
            s1 += val
            q1.append(val)
            
        answer += 1
        
    return answer