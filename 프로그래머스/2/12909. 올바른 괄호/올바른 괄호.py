def solution(s):
    stack = []
    for parentheses in s:
        if parentheses == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return not stack

# 100,000 이하 -> O(nlogn) 이하
# 괄호 -> Stack
# False가 되는 경우 : (가 없는데 ) 나오는 경우, (가 남는 경우
# 시간복잡도 : O(n)