from itertools import permutations
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)
    candidates = set()

    for length in range(1, len(nums) + 1):
        for perm in permutations(nums, length):
            n = int(''.join(perm))
            candidates.add(n)

    count = 0
    for n in candidates:
        if is_prime(n):
            count += 1

    return count