def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        goal_time = schedules[i]
        
        limit_m = (goal_time // 100) * 60 + (goal_time % 100) + 10
        
        is_perfect = True
        for day_idx, log in enumerate(timelogs[i]):
            current_day = (startday + day_idx - 1) % 7 + 1
            
            if current_day >= 6:
                continue
            
            log_m = (log // 100) * 60 + (log % 100)
            
            if log_m > limit_m:
                is_perfect = False
                break
        
        if is_perfect:
            answer += 1
            
    return answer