def solution(s):
    data = s[2:-2].split("},{")
    
    data.sort(key=len)
    
    answer = []
    check = set()
    
    for row in data:
        nums = row.split(",")
        for n in nums:
            val = int(n)
            if val not in check:
                answer.append(val)
                check.add(val)
                
    return answer