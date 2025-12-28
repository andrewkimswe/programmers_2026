def solution(numbers):
    numbers = list(map(str, numbers))
    
    # x*3을 기준으로 내림차순 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(numbers)
    
    return str(int(answer))