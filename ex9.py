annual_salary = float(input("Please input your annual salary"))
tempsal = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
deposit = total_cost * 0.25
months_to_save = 36
months_saving = 0
current_savings = 0
interest = 0.04

leeway = 100
high_leeway = 1
lowleeway = 0
guess = (highleeway+lowleeway) / 2
step = 0

portion_saved = 0

while portion_saved < deposit - leeway or portion_saved > deposit + leeway:
	#quick base case for if they can't afford the house deposit in 36 months
	for x in range(1, months_to_save+1):
		current_savings += (annual_salary/12) * guess # monthly salary portion added to savings
		current_savings += current_savings*interest/12 # monthly interest added to savings
		months_saving += 1 # month count
		if months_saving%6 == 0:
			annual_salary += annual_salary*semi_annual_raise # every 6 months increase salary
	if current_savings < deposit:
		print("Cannot afford the deposit in 36 months")
		break
	current_savings = 0
	months_saving = 0       #resets calculated values in for loop
	annual_salary = tempsal
	for x in range(1, months_to_save+1):
		current_savings += (annual_salary/12) * guess # monthly salary portion added to savings
		current_savings += current_savings*interest/12 # monthly interest added to savings
		months_saving += 1 # month count
		if months_saving%6 == 0:
			annual_salary += annual_salary*semi_annual_raise # every 6 months increase salary
	portion_saved = current_savings # keeps things seperate and clean
	if portion_saved > deposit - leeway and portion_saved < deposit + leeway:

		print("You need to save " + str(round(guess,2) * 100) + "% of your earnings every month") # this works
		print("Steps in bisection search: " + str(step))
		break
	elif portion_saved < deposit - leeway: # saving too little money
		lowleeway = guess
	else: # saving too much money
		highleeway = guess
	guess = (highleeway+lowleeway) / 2
	step += 1
