
def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("leap year")
            else:
                print("not leap year")
        else:
                print("not leap year")  
    else:
                print("not leap year")                     
def days_in_month(year,month):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]
year=int(input("enter the year"))
month=int(input("enter the month"))
days=days_in_month(year,month)
print(days)