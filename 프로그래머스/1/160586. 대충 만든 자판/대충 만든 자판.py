def solution(keymap, targets):
    
    min_press = {}
    
    for key in keymap:
        for i, char in enumerate(key):
            if char not in min_press:
                min_press[char] = i + 1
            else:
                min_press[char] = min(min_press[char], i + 1)
    
    answer = []
    
    for target in targets:
        total_count = 0
        for char in target:
            if char in min_press:
                total_count += min_press[char]
            else:
                total_count = -1
                break
        answer.append(total_count)
    
    return answer