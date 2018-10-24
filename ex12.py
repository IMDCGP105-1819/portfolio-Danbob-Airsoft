#Defining functions for later use
def Hotel_Cost(Nights):
    return 70 * Nights
def Plane_Ticket_Cost(City,Seat_Class):
    if City == "New York":
        return 2000 * Seat_Class
    if City == "Auckland":
        return 790 * Seat_Class
    if City == "Venice":
        return 154 * Seat_Class
    if City == "Glasgow":
        return 65 * Seat_Class
def Rental_Car_Cost(Days):
    if Days > 7:
        return 30 * Days - 50
    elif Days > 3:
        return 30 * Days - 30
    else:
        return 30 * Days
#calling functions to use in combination
def Total_Cost(city, days):
    return Hotel_Cost(days) + Plane_Ticket_Cost(city, grade) + Rental_Car_Cost(days)
#collects user inputs for functions
city = input("Where do you want to go? ")
grade = input("What class do you want to fly in? ")
days = input("How many days are you going for? ")

print(Total_Cost(city, days))
