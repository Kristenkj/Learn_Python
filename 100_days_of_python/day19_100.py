
loan = 1000
annual_percentage_rate = 0.05

for i in range (10):
  loan += (loan * annual_percentage_rate)
  print("Year", i+1, ": ", round(loan, 2))

print()