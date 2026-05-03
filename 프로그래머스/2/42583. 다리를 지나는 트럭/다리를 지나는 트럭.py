from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    on_weight = 0
    on_bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    
    while waiting:
        time += 1
        
        left = on_bridge.popleft()
        on_weight -= left
        
        if on_weight + waiting[0] <= weight:
            truck = waiting.popleft()
            on_bridge.append(truck)
            on_weight += truck
        else:
            on_bridge.append(0)
    
    return time + bridge_length