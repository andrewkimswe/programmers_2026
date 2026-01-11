def solution(friends, gifts):
    n = len(friends)

    name_to_idx = {name: i for i, name in enumerate(friends)}
    
    graph = [[0] * n for _ in range(n)]
    gift_indices = [0] * n
    
    for g in gifts:
        giver, receiver = g.split()
        idx1, idx2 = name_to_idx[giver], name_to_idx[receiver]
        graph[idx1][idx2] += 1
        gift_indices[idx1] += 1
        gift_indices[idx2] -= 1
        
    next_month_gifts = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] > graph[j][i]:
                next_month_gifts[i] += 1
            elif graph[i][j] < graph[j][i]:
                next_month_gifts[j] += 1
            else:
                if gift_indices[i] > gift_indices[j]:
                    next_month_gifts[i] += 1
                elif gift_indices[i] < gift_indices[j]:
                    next_month_gifts[j] += 1
                    
    return max(next_month_gifts)