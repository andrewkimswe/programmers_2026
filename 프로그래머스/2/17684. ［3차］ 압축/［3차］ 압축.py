def solution(msg):
    answer = []
    alphabet_dict = {chr(i): i - 64 for i in range(ord('A'), ord('Z') + 1)}
    start = 0
            
    while start < len(msg):
        end = start + 1
        
        while end <= len(msg) and msg[start:end] in alphabet_dict:
            end += 1
            
        w = msg[start:end-1]
        answer.append(alphabet_dict[w])
        
        if end <= len(msg):
            new_word = msg[start:end]
            alphabet_dict[new_word] = len(alphabet_dict) + 1
        
        start += len(w)
    
    return answer