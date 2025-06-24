import datetime
from datetime import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")
    return current_date
current_date = display_current_datetime()

number_of_days = int(input("Please Enter a number of days: "))

def calculate_future_date(current_date, number_of_days):
    future_date = current_date.date() + timedelta(days=number_of_days)
    print(f"Future date after {number_of_days} days: {future_date}")
future_date = calculate_future_date(current_date, number_of_days)