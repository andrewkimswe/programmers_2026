def solution(n, lost, reserve):
    actual_lost = sorted(list(set(lost) - set(reserve)))
    actual_reserve = set(reserve) - set(lost)
    
    lost_count = len(actual_lost)
    
    for student in actual_lost:
        if student - 1 in actual_reserve:
            actual_reserve.remove(student - 1)
            lost_count -= 1
        elif student + 1 in actual_reserve:
            actual_reserve.remove(student + 1)
            lost_count -= 1
    
    return n - lost_count