def solution(video_len, pos, op_start, op_end, commands):
    
    def to_num(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def to_str(n):
        h, m = divmod(n, 60)
        return f"{h:02d}:{m:02d}"

    def check_opening(curr, start, end):
        if start <= curr <= end:
            return end
        return curr

    curr_n = to_num(pos)
    start_n = to_num(op_start)
    end_n = to_num(op_end)
    limit_n = to_num(video_len)

    curr_n = check_opening(curr_n, start_n, end_n)

    for cmd in commands:
        if cmd == "next":
            curr_n = min(limit_n, curr_n + 10)
        else:
            curr_n = max(0, curr_n - 10)
            
        curr_n = check_opening(curr_n, start_n, end_n)

    return to_str(curr_n)