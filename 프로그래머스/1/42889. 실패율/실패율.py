def solution(N, stages):
    fail_rates = {}
    total_players = len(stages)
    
    for i in range(1, N + 1):
        if total_players > 0:
            count = stages.count(i)
            fail_rates[i] = count / total_players
            total_players -= count
        else:
            fail_rates[i] = 0
            
    return sorted(fail_rates, key=lambda x : fail_rates[x], reverse=True)