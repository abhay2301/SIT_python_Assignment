reference_year=1900
reference_day=1
year=int(input('Enter a year'))
year_difference=year- reference_year
leap_years=0
non_leap_year = 0
for i in range(reference_year,year):
    if(i%4==0 and i%100!=0) or (i%400==0):
        leap_years+=1
    else:
        non_leap_year+=1
odd_days = (leap_years*2 + non_leap_year*1) % 7
dya_of_week=(reference_day + odd_days)%7          