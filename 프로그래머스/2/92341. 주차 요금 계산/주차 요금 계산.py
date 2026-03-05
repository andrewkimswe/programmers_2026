import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    parking_log = {}
    total_times = {}
    
    for record in records:
        time_str, car_num, status = record.split()
        h, m = map(int, time_str.split(':'))
        curr_time = h * 60 + m
        
        if status == "IN":
            parking_log[car_num] = curr_time
        else:
            duration = curr_time - parking_log.pop(car_num)
            total_times[car_num] = total_times.get(car_num, 0) + duration
            
    for car_num, in_time in parking_log.items():
        duration = 1439 - in_time
        total_times[car_num] = total_times.get(car_num, 0) + duration
        
    answer = []
    for car_num in sorted(total_times.keys()):
        time = total_times[car_num]
        if time <= base_time:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((time - base_time) / unit_time) * unit_fee
        answer.append(fee)
        
    return answer