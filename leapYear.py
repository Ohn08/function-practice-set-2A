def is_leap_year(year):
    """
    Determine whether a given year is a leap year.

    A leap year is a year that is evenly divisible by 4, except for years that are both divisible
    by 100 and not divisible by 400.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input
year_to_check = int(input("Enter a year: "))
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")