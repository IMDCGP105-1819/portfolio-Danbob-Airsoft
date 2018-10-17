Total_Cost = float (input ("How much does your dream home cost? "))
Portion_deposit = Total_Cost * 0.20
Current_Savings = 0
Annual_Salary = float(input ("What is your annual salary? "))
Portion_Saved = float(input ("How much of your salary (as a decimal) would you like to save? "))
Monthly_Salary = Annual_Salary /12
Monthly_Saving = Monthly_Salary * Portion_Saved
Months_To_Save = 0
semi_annaul_sallery = float(input("Please input your semi annual raise "))

while Current_Savings < Total_Cost:
    Current_Savings = Current_Savings + Monthly_Saving
    Current_Savings += Current_Savings * 1.04/12
    Months_To_Save = Months_To_Save + 1
    if Months_To_Save % 6 == 0:
        Annual_Salary += Annual_Salary * (semi_annaul_sallery)
print (f"It will take {Months_To_Save} months to save for this home")
