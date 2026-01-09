def change_notes(melody):
    return (melody.replace('C#', 'c')
                  .replace('D#', 'd')
                  .replace('F#', 'f')
                  .replace('G#', 'g')
                  .replace('A#', 'a')
                  .replace('E#', 'e')
                  .replace('B#', 'b'))

def solution(m, musicinfos):
    m = change_notes(m)
    candidates = []
    
    for idx, info in enumerate(musicinfos):
        start, end, title, sheet = info.split(',')
        
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        duration = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        
        sheet = change_notes(sheet)
        full_melody = (sheet * (duration // len(sheet) + 1))[:duration]
        
        if m in full_melody:
            candidates.append((duration, idx, title))
            
    if not candidates:
        return "(None)"
    
    candidates.sort(key=lambda x: (-x[0], x[1]))
    
    return candidates[0][2]