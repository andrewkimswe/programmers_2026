def solution(players, callings):
    
    rank_dict = {player: i for i, player in enumerate(players)}
        
    for name in callings:
        current_rank = rank_dict[name]
        prev_rank = current_rank - 1
        prev_player = players[prev_rank]
        
        players[prev_rank], players[current_rank] = players[current_rank], players[prev_rank]
        
        rank_dict[name] = prev_rank
        rank_dict[prev_player] = current_rank
        
    return players