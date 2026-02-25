def solution(id_list, report, k):
    report = set(report)
    
    report_hist = {user: [] for user in id_list}
    mail_count = {user: 0 for user in id_list}
    
    for r in report:
        reporter, reported = r.split()
        report_hist[reported].append(reporter)
    
    for reported, reporters in report_hist.items():
        if len(reporters) >= k:
            for user in reporters:
                mail_count[user] += 1
                
    return [mail_count[user] for user in id_list]