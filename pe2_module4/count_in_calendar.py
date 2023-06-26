import calendar


class invalidWeekDay(Exception):
    """Raised when inputted weekday is less than 0 or more than 6"""
    pass


class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year, weekday):
        try:
            if 0 <= weekday <= 6:
                count = month_in_a_year = 0
                while month_in_a_year < 12:
                    month_in_a_year += 1
                    for data in self.monthdays2calendar(year, month_in_a_year):
                        for date in data:
                            if date[0] != 0 and date[1] == weekday:
                                count += 1
                            else:
                                continue
                print(count)
            else:
                raise invalidWeekDay
        except invalidWeekDay:
            print("Please enter the weekday number between 0-6.")


my_calendar = MyCalendar()
my_calendar.count_weekday_in_year(int(input('year=')), int(input('weekday=')))
