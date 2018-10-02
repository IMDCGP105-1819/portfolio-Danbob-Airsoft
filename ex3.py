Cars = 100
Space_In_Car = 4.0
Drivers = 30
Passengers = 90
Cars_Not_Driven = Cars - Drivers
Cars_Driven = Drivers
Carpool_Capacity = Cars_Driven * Space_In_Car
Average_Passengers_Per_Car = Passengers / Cars_Driven #Error in example is missing S on passengers

print("There are", Cars, "cars available.")
print("There are only", Drivers, "drivers available.")
print("There will be", Cars_Not_Driven, "empty cars today.")
print("We can transport", Carpool_Capacity, "people today.")
print("We have", Passengers, "to carpool today.")
print("We need to put about", Average_Passengers_Per_Car, "in each car.")
