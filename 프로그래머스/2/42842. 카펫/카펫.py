def solution(brown, yellow):
    S = (brown + 4) // 2
    P = brown + yellow
    
    D = (S**2 - 4*P)**0.5
    
    x = (S + D) // 2
    y = (S - D) // 2
    
    return [int(x), int(y)]