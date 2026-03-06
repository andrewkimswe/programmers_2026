def solution(record):
    user_info = {}
    log = []
    
    for r in record:
        split_r = r.split()
        command = split_r[0]
        user_id = split_r[1]
        
        if command in ("Enter", "Change"):
            user_info[user_id] = split_r[2]
            
        if command in ("Enter", "Leave"):
            log.append((command, user_id))
            
    answer = []
    for command, user_id in log:
        if command == "Enter":
            answer.append(f"{user_info[user_id]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{user_info[user_id]}님이 나갔습니다.")
            
    return answer