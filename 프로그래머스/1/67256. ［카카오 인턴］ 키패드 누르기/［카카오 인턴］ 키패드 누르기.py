def solution(numbers, hand):
    
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    cur_left = keypad['*']
    cur_right = keypad['#']
    answer = ''

    for n in numbers:
        target = keypad[n]
        
        if n in [1, 4, 7]:
            answer += 'L'
            cur_left = target
            
        elif n in [3, 6, 9]:
            answer += 'R'
            cur_right = target
            
        else:
            dist_l = abs(cur_left[0] - target[0]) + abs(cur_left[1] - target[1])
            dist_r = abs(cur_right[0] - target[0]) + abs(cur_right[1] - target[1])
            
            if dist_l < dist_r:
                answer += 'L'
                cur_left = target
                
            elif dist_r < dist_l:
                answer += 'R'
                cur_right = target
                
            else:
                
                if hand == "left":
                    answer += 'L'
                    cur_left = target
                    
                else:
                    answer += 'R'
                    cur_right = target
                    
    return answer