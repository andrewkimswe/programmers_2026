def solution(survey, choices):
    scores = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
                   
    for s, c in zip(survey, choices):
        if c < 4:
            scores[s[0]] += (4 - c)
        elif c > 4:
            scores[s[1]] += (c - 4)

    indicators = ["RT", "CF", "JM", "AN"]
    answer = ''
    
    for pair in indicators:
        diff = scores[pair[0]] - scores[pair[1]]
        
        if diff >= 0:
            answer += pair[0]
        else:
            answer += pair[1]
            
    return answer