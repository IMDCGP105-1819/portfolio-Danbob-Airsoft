Total_Cost = float (input ("How much does your dream home cost? "))
Portion_deposit = Total_Cost * 0.20
Current_Savings = 0
Annual_Salary = float(input ("What is your annual salary? "))
Portion_Saved = float(input ("How much of your salary (as a decimal) would you like to save? "))
Monthly_Salary = Annual_Salary /12
Monthly_Saving = Monthly_Salary * Portion_Saved
Months_To_Save = 0

while Current_Savings < Total_Cost:
    Current_Savings = Current_Savings + Monthly_Saving
    Current_Savings += Current_Savings * 1.04/12
    Months_To_Save = Months_To_Save + 1
print (f"It will take {Months_To_Save} months to save for this home")
