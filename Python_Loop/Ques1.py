'''Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs. 
12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for 
fractional part of an hour. '''

num_employee=10

overtime_rate=12.00

for i in range(1,num_employee,+1):
    hour_work=int(input(f"Enter overtime worked by employee {i}: "))
    
    if hour_work>40:
        overtime_hour=hour_work - 40
        print("Overtime worked by the employee: ",overtime_hour)
        overrtime_payment=overtime_hour * overtime_rate
        print('payment=',overrtime_payment)
    else:
        print('No overtime so Payment=0.0')
        
    