import math

def to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    
    parking_status = {}
    total_times = {}
    
    for r in records:
        time, car_num, status = r.split()
        minutes = to_minutes(time)
        
        if status == "IN":
            parking_status[car_num] = minutes
            if car_num not in total_times:
                total_times[car_num] = 0
        else:
            total_times[car_num] += minutes - parking_status[car_num]
            del parking_status[car_num]
            
    last_time = to_minutes("23:59")
    for car_num, in_time in parking_status.items():
        total_times[car_num] += last_time - in_time
        
    sorted_cars = sorted(total_times.items())
    
    answer = []
    for car_num, total_time in sorted_cars:
        fee = base_fee
        
        if total_time > base_time:
            fee += math.ceil((total_time - base_time) / unit_time) * unit_fee
            
        answer.append(fee)
            
    return answer