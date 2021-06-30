from datetime import datetime
def AgeFinder():
    birth_year = int(input("Enter the year in which you were born  : "))
    birth_month = int(input("Enter the month in which you were born : "))
    birth_date = int(input("Enter the day on which you were born : "))
    birthday = datetime(birth_year,birth_month,birth_date,0,0,0)
    today = datetime.today()
    result = today - birthday
    days = result.days
    print(f"You have lived {days} days")
    print(f"You have lived {days*24} hours")
    print(f"You have lived {days*24*60} minutes")
    print(f"You have lived {days*24*60*60} seconds")
    
AgeFinder()
    
    