def solution(files):
    answer = []
    parsed = []
    
    for i, file in enumerate(files):
        head, number, tail = "", "", ""

        idx = 0
        while not file[idx].isdigit():
            idx += 1
        head = file[:idx]
        
        start_num = idx
        while idx < len(file) and file[idx].isdigit():
            idx += 1
            if idx - start_num == 5:
                break
        
        number = file[start_num:idx]
        tail = file[idx:]
        
        parsed.append((head.lower(), int(number), i, file))
    
    parsed.sort(key=lambda x: (x[0], x[1]))
    
    return [p[3] for p in parsed]