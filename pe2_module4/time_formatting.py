import datetime

def format_time(input_datetime):
    print(input_datetime.strftime('%Y/%m/%d %H:%M:%S'))
    print(input_datetime.strftime('%y/%B/%d %H:%M:%S %p'))
    print(input_datetime.strftime('%a, %Y %b %d'))
    print(input_datetime.strftime('%A, %Y %B %d'))
    print(input_datetime.strftime('Weekday: %w'))
    print(input_datetime.strftime('Day of the year: %j'))
    print(input_datetime.strftime('Week number of the year: %U'))

dt = datetime.datetime(2020, 11, 4, 14, 53)
format_time(dt)
