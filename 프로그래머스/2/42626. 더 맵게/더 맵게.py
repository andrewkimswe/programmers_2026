import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_food = first + second * 2
        heapq.heappush(scoville, new_food)
        count += 1

    return count