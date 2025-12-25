from collections import defaultdict

def solution(genres, plays):
    answer = []
    total_plays = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        total_plays[g] += p
        genre_songs[g].append((p, i))
    
    # 1. 장르 정렬 (아이템을 꺼내서 값(x[1]) 기준으로 정렬)
    sorted_genres = sorted(total_plays.items(), key=lambda x: x[1], reverse=True)
    
    # 2. 장르별 곡 정렬 및 추출
    for genre, _ in sorted_genres:
        # 재생수 내림차순(-), 고유번호 오름차순(+)
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        answer.extend([s[1] for s in songs[:2]])

    return answer