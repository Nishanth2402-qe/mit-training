import datetime

def calculate_age(birth_date_str):
    try:
        birth_date = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d")
        current_date = datetime.datetime.now()
        time_diff = current_date - birth_date
        years = time_diff.days // 365
        remaining_days = time_diff.days % 365
        total_hours = time_diff.total_seconds() // 3600
        total_minutes = time_diff.total_seconds() // 60
        remaining_minutes = int(total_minutes % (24 / 60))
        
        return {
            "years": years,
            "days": remaining_days,
            "hours": int(total_hours % 12),
            "minutes": remaining_minutes
        }
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

def main():
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    result = calculate_age(birth_date)
    
    if isinstance(result, dict):
        print(f"Your age is: {result['years']} years, {result['days']} days, "
              f"{result['hours']} hours, and {result['minutes']} minutes")
    else:
        print(result)

if __name__ == "__main__":
    main()