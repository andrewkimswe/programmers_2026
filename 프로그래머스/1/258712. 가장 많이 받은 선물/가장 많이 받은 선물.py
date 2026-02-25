def solution(friends, gifts):
    record = {f: {f2: 0 for f2 in friends} for f in friends}

    gift_score = {f: 0 for f in friends}
    
    next_month = {f: 0 for f in friends}

    for g in gifts:
        giver, receiver = g.split()
        record[giver][receiver] += 1
        gift_score[giver] += 1
        gift_score[receiver] -= 1
        
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            f1 = friends[i]
            f2 = friends[j]
            
            give_f1 = record[f1][f2]
            give_f2 = record[f2][f1]
            
            if give_f1 > give_f2:
                next_month[f1] += 1
            elif give_f2 > give_f1:
                next_month[f2] += 1
            else:
                if gift_score[f1] > gift_score[f2]:
                    next_month[f1] += 1
                elif gift_score[f2] > gift_score[f1]:
                    next_month[f2] += 1

    return max(next_month.values())