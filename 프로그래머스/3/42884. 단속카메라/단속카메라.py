def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    last_camera = -30001
    for route in routes:
        if route[0] > last_camera:
            answer += 1
            last_camera = route[1]
            
    return answer

# 고속도로 차량 경로 routes IN -> out
# at least 단속 카메라 한번
# 몇대의 카메라 설치 필요할까?
# 차량 1대 이상 10000대 이하
# 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라 만난것 간주
# 진입 진출 시점은 -30,000 이상 30,000 이하

# 겹치는 범위에 설치하면 유리할듯?
# 겹치는거 뒷 부분 기준으로 하는게
# 