import re
from itertools import permutations

def solution(expression):
    answer = 0
    numbers = list(map(int, re.split('([^0-9])', expression)[::2]))
    operators = re.split('[0-9]+', expression)[1:-1]
    perms = list(permutations(['+', '-', '*'], 3))
    for perm in perms:
        temp_nums = numbers[:]
        temp_ops = operators[:]
        
        for operator in perm:
            while operator in temp_ops:
                idx = temp_ops.index(operator)
            
                if operator == '+':
                    res = temp_nums[idx] + temp_nums[idx+1]
                elif operator == '-':
                    res = temp_nums[idx] - temp_nums[idx+1]
                else:
                    res = temp_nums[idx] * temp_nums[idx+1]
            
                temp_nums[idx] = res
                del temp_nums[idx+1]
                del temp_ops[idx]
            
        answer = max(answer, abs(temp_nums[0]))
    return answer