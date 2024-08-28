# This solution differs from the documented solution in that 
# this logic accounts for a leap year every four years
def life_in_weeks(age):
    years_left = years_lifespan - age
    days_left = int((years_left * 365) + (years_left / 4))
    weeks_left = int(days_left / 7)
    print(f"You have {weeks_left} weeks left.")


age = int(input("What is your current age? "))

years_lifespan = 90

life_in_weeks(age)





