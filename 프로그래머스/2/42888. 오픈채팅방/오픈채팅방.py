def solution(record):
    answer = []
    user_db = {}
    
    for r in record:
        info = r.split()
        if info[0] in ['Enter', 'Change']:
            user_db[info[1]] = info[2]
    
    for r in record:
        info = r.split()
        if info[0] == 'Enter':
            answer.append(f"{user_db[info[1]]}님이 들어왔습니다.")
        elif info[0] == 'Leave':
            answer.append(f"{user_db[info[1]]}님이 나갔습니다.")
    return answer