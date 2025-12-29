def solution(answers):
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == answer_1[i % len(answer_1)]:
            scores[0] += 1
        if ans == answer_2[i % len(answer_2)]:
            scores[1] += 1
        if ans == answer_3[i % len(answer_3)]:
            scores[2] += 1
    
    max_score = max(scores)
    
    result = []
    for i, s in enumerate(scores):
        if s == max_score:
            result.append(i + 1)
            
    return result