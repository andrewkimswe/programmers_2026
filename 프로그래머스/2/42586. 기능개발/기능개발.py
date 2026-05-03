import math

def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
    
    answer = []
    current_max = days[0]
    count = 1

    for d in days[1:]:
        if d <= current_max:
            count += 1
        else:
            answer.append(count)
            current_max = d
            count = 1

    answer.append(count)
    return answer