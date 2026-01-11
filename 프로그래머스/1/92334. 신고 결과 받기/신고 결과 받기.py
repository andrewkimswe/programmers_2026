def solution(id_list, report, k):
    answer = []
    report = set(report)
    
    report_count = {id: 0 for id in id_list}
    user_reports = {id: [] for id in id_list}
    
    for r in report:
        reporter, reported = r.split()
        report_count[reported] += 1
        user_reports[reporter].append(reported)
    
    for id in id_list:
        mail = 0
        for reported_user in user_reports[id]:
            if report_count[reported_user] >= k:
                mail += 1
        answer.append(mail)
        
    return answer