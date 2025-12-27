from collections import deque

def solution(progresses, speeds):
    answer = []
    # 배포는 하루에 최대 한 번
    queue = deque([(100 - p + s - 1) // s for p, s in zip(progresses, speeds)])
    while queue:
        x = queue.popleft()
        count = 1
        while queue and queue[0] <= x:
            queue.popleft()
            count += 1
        answer.append(count)
    return answer

# Time Complexity : O(N)