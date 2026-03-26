def solution(n):
    answer = []
    odd = 1
    while n >= odd:
        answer.append(odd)
        odd = odd + 2
    return answer