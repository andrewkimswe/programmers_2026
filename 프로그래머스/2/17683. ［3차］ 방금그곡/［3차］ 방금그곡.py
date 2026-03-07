def change_note(s):
    return s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('B#', 'b')

def solution(m, musicinfos):
    m = change_note(m)
    candidates = []

    for i, info in enumerate(musicinfos):
        start, end, title, melody = info.split(',')
        
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        play_time = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        
        melody = change_note(melody)
        full_melody = (melody * (play_time // len(melody) + 1))[:play_time]
        
        if m in full_melody:
            candidates.append((play_time, i, title))
            
    if not candidates:
        return "(None)"
    
    candidates.sort(key=lambda x: (-x[0], x[1]))
    
    return candidates[0][2]