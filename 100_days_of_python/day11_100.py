secs = 60
mins = 60
hours = 24
month = 31
year = 365
leap_year = 366

secs_in_year = (hours * 3600) * year
secs_in_leap_year = (hours * 3600) * leap_year

print(f"There are {secs_in_year} seconds in a year and {secs_in_leap_year} seconds in a leap year")