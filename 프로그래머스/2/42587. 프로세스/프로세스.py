from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    order = 0
    
    while queue:
        cur = queue.popleft()
        
        if queue and cur < max(queue):
            queue.append(cur)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
        else:
            order += 1
            if location == 0:
                return order
            else:
                location -= 1