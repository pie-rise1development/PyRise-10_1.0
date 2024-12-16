import calendar
from datetime import datetime

def print_calendar(year, month):
    cal = calendar.TextCalendar(calendar.MONDAY)
    cal_str = cal.formatmonth(year, month)
    return cal_str

def get_current_date():
    now = datetime.now()
    return now.strftime('%Y-%m-%d')

def main():
    year = int(input('Введите год о котором хотите узнать информацию: '))
    month =int(input("Введите месяц года, который вы указали ранее: "))

    current_date = get_current_date()
    print(f"Это реальная дата, которая сегодня: {current_date}\n")
    print("-")
    print("")
    print("-")
    print("А это дата, которую вы указали в поисковике: \n")
    print("")
    calendar_output = print_calendar(year, month)
    print(calendar_output)
    print("")

if __name__ == "__main__":
    main()

