def solution(citations):
    citations.sort()
    n = len(citations)
    h = 0

    for i, c in enumerate(citations):
        cnt = n - i
        if c >= cnt:
            h = cnt
            break

    return h