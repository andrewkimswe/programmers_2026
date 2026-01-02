def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    last_camera = -30001
    for route in routes:
        if route[0] > last_camera:
            answer += 1
            last_camera = route[1]
            
    return answer
