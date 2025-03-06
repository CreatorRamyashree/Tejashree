import calendar

def display_months():
    months = list(calendar.month_name)[1:]
    for month in months:
        print(month)

display_months()