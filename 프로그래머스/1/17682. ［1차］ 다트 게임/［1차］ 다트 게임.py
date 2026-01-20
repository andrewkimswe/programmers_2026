def solution(dartResult):
    dartResult = dartResult.replace('10', 'K')
    scores = []
            
    for i in dartResult:
        if i.isdigit() or i == 'K':
            num = 10 if i == 'K' else int(i)
            scores.append(num)
            
        elif i == 'S':
            scores[-1] = scores[-1] ** 1
        elif i == 'D':
            scores[-1] = scores[-1] ** 2
        elif i == 'T':
            scores[-1] = scores[-1] ** 3
            
        elif i == '*':
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2
        elif i == '#':
            scores[-1] *= -1
            
    return sum(scores)