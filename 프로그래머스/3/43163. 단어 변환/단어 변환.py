from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        curr_word, step = queue.popleft()
        
        if curr_word == target:
            return step
        
        for word in words:
            if word not in visited:
                
                diff = 0
                for i in range(len(curr_word)):
                    if curr_word[i] != word[i]:
                        diff += 1
                        
                if diff == 1:
                    visited.add(word)
                    queue.append((word, step + 1))
                    
    return 0