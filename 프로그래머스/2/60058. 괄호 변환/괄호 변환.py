def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if not p:
        return ""

    # 2. 문자열 p를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    u, v = split_uv(p)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 v에 대해 1단계부터 다시 수행합니다.
    if is_correct(u):
        return u + solution(v)
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        answer = '('              # 4-1
        answer += solution(v)     # 4-2
        answer += ')'              # 4-3
        
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 붙입니다.
        u_content = u[1:-1]
        for char in u_content:
            if char == '(':
                answer += ')'
            else:
                answer += '('
        return answer

# --- 보조 함수들 ---
def split_uv(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(': count += 1
        else: count -= 1
        if count == 0:
            return p[:i+1], p[i+1:]

def is_correct(u):
    stack = 0
    for char in u:
        if char == '(':
            stack += 1
        else:
            if stack == 0:
                return False
            stack -= 1
    return True