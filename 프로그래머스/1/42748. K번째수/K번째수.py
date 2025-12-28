def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        tmp_ary = array[i-1:j]
        tmp_ary.sort()
        answer.append(tmp_ary[k-1])
    return answer