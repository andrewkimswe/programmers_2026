def is_prime_number(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    s = ""
    while n:
        s = str(n % k) + s
        n //= k
        
    data = s.split('0')
    answer = 0
    
    for val in data:
        if val and is_prime_number(int(val)):
            answer += 1
            
    return answer