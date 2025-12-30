from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    all_nums = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for p in perms:
            all_nums.add(int("".join(p)))
            
    count = 0
    for num in all_nums:
        if is_prime(num):
            count += 1
            
    return count