from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]
    
    for p in product(discounts, repeat=len(emoticons)):
        plus_user = 0
        total_sales = 0
        
        for user_rate, user_limit in users:
            user_spent = 0
            for i in range(len(emoticons)):
                if p[i] >= user_rate:
                    user_spent += emoticons[i] * (100 - p[i]) // 100
            
            if user_spent >= user_limit:
                plus_user += 1
            else:
                total_sales += user_spent
        
        if plus_user > answer[0]:
            answer = [plus_user, total_sales]
        elif plus_user == answer[0] and total_sales > answer[1]:
            answer[1] = total_sales
            
    return answer