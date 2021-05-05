print("Welcome to Leap Year Checker!!")
year = int(input("Please, Enter the Year: "))

# Check if year is totally Divisible By 4.
if year % 4 == 0:
    # Check if year is totally Divisible By 100.
    if year % 100 == 0:
        # Check if year is totally Divisible by 400.
        if year % 400 == 0:
            # If year is divisible by 400 Then it's a Leap Year.
            print(f"The Year {year} is a leap year.")
        else:
            # If year is divisible by 100 and not by 400 then it's not a leap year.
            print(f"The Year {year} is not a leap year.")
    else:
        # If year is divisible by 4 then it's a leap year (also keep above 2 conditions in mind).
        print(f"The Year {year} is a leap year.")
else:
    # If year is not divisible by 4 then it's not a Leap year.
    print(f"The Year {year} is not a leap year.")