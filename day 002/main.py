print("welcome to the tip calucate")
bill = float(input("what was a total bill ? "))
people = int(input("how many people to split the bill ? "))
tip = int(input("what percentage tip would you like to give? 10,12,15? "))

#محاسبه مبلغ انعام 
tip_as_percent = bill / 100
total_tip_amount = tip_as_percent * 12

total_bill = bill + total_tip_amount
#محاسبه مبلغ کل
bill_per_person = total_bill / people
#مبلغ کل تا ی رقم اعشار
final_amount = round(bill_per_person , 2)
print(f"each person should pay : {final_amount}")




