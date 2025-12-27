def solution(arr):
    answer = []
    for x in arr:
        if not answer or x != answer[-1]: # len(answer) == 0도 됨.
            answer.append(x)
    return answer