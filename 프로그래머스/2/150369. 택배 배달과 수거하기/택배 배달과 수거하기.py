def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_rem = 0
    p_rem = 0
    
    for i in range(n - 1, -1, -1):
        d_rem -= deliveries[i]
        p_rem -= pickups[i]
        
        cnt = 0
        while d_rem < 0 or p_rem < 0:
            d_rem += cap
            p_rem += cap
            cnt += 1
        
        answer += cnt * (i + 1) * 2
        
    return answer