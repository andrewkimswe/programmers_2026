def convert(num, n):
    if num == 0:
        return "0"
    chars = "0123456789ABCDEF"
    res = ""
    while num > 0:
        res = chars[num % n] + res
        num //= n
    return res

def solution(n, t, m, p):
    all_stream = ""
    num = 0
    while len(all_stream) < m * t:
        all_stream += convert(num, n)
        num += 1
        
    answer = all_stream[p-1 : m*t : m]
    
    return answer