def solution(new_id):
    new_id = new_id.lower() # 1단계
    
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    new_id = "".join([c for c in new_id if c in allowed]) # 2단계
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.') # 3단계
        
    new_id = new_id.strip('.') # 4단계
    
    if not new_id:
        return "aaa" # 5단계
    
    new_id = new_id[:15].rstrip('.') # 6단계
    
    while len(new_id) < 3:
        new_id += new_id[-1] # 7단계
        
    return new_id