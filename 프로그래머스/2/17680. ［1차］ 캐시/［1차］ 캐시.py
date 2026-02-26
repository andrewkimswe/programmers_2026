from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
            
        else:
            answer += 5
            cache.append(city)
            
    return answer