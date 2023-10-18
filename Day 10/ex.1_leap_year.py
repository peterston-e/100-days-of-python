def is_leap(year):
    """works out if its a leap year"""
    # Docstring above

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# TODO: Add more code here 👇
# INPUTS HARD CODED FOR TESTING


def days_in_month(inp_year, inp_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(inp_year) and inp_month == 2:
        return month_days[inp_month - 1] + 1
    else:
        return month_days[inp_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
