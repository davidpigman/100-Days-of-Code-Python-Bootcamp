# This is how you work out whether if a particular year is a leap year. 
# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder 
# unless the year is also divisible by 400 with no remainder   

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    year = int(year)
    leap_year_4 = year % 4
    leap_year_100 = year % 100
    leap_year_400 = year % 400
    bln_leap_year = False

    #Debug Statements
    #print(f"leap year 4 {leap_year_4}")
    #print(f"leap year 100 {leap_year_100}")
    #print(f"leap year 400 {leap_year_400}")

    if leap_year_4 == 0:
      bln_leap_year = True
      if leap_year_100 == 0:
         if leap_year_400 == 0:
            bln_leap_year = True
         else:
            bln_leap_year = False
    
    return bln_leap_year

year = input("Enter the year to determine if it is a leap year: ")
leap_year = is_leap_year(year)
print(leap_year)
