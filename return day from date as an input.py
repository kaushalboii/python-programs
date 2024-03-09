import datetime

def get_day_of_week(day, month, year):
    # Create a datetime object for the given date
    given_date = datetime.datetime(year, month, day)
    # Get the weekday index (0 for Monday, 1 for Tuesday, ..., 6 for Sunday)
    weekday_index = given_date.weekday()
    # Map weekday index to corresponding weekday name
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[weekday_index]
print("Enter date, month and year")
day = int(input())
month = int(input())
year = int(input())
print("Curresponding day: ", get_day_of_week(day, month, year))
