try:
  hours = float(input("Enter Hours: "))
  rate =  float(input("Enter Rate: "))
except ValueError:
   print("Error, please enter numeric input for Rate")
   quit()
else:
  overtime = hours-40
  if hours > 40:
    total_overtime_pay =round(40*rate+overtime*rate* 1.5, 2)
    print(f"pay: {total_overtime_pay}" )
  else:
    pay = round(hours * rate, 2)
    print(f"pay: {pay}")
