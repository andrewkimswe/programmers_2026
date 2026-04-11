def solution(nums):
    pick_limit = len(nums) // 2
    
    unique_types = len(set(nums))
    
    return min(pick_limit, unique_types)