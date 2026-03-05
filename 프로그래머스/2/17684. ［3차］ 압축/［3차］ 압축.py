def solution(msg):
    dic = {chr(i + 64): i for i in range(1, 27)}
    
    answer = []
    start, end = 0, 1
    next_index = 27
    
    while end <= len(msg):
        w = msg[start:end]
        
        if w in dic:
            end += 1
        else:
            answer.append(dic[w[:-1]])
            dic[w] = next_index
            next_index += 1
            start = end - 1
            
    answer.append(dic[msg[start:]])
    
    return answer