def solution(today, terms, privacies):
    answer = []
    
    def convert_to_days(date_str):
        y, m, d = map(int, date_str.split('.'))
        return (y * 12 * 28) + (m * 28) + d
    
    today_total = convert_to_days(today)
    
    terms_dict = {}
    for term in terms:
        name, month = term.split()
        terms_dict[name] = int(month)
        
    for i, privacy in enumerate(privacies):
        date_part, term_name = privacy.split()
        start_total = convert_to_days(date_part)
        
        expiry_total = start_total + (terms_dict[term_name] * 28)
        
        if expiry_total <= today_total:
            answer.append(i + 1)
            
    return answer