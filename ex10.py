Numberlow = int(input("Please input the low end of your range "))
Numberhigh = int(input("Please input the high end of your range "))
for Number in range(Numberlow,Numberhigh + 1):
    if Number % 3 == 0 and Number % 5 == 0:
        print ("FizzBuzz")
    elif Number % 3 ==0:
        print ("Fizz")
    elif Number % 5 == 0:
        print ("Buzz")
    else:
        print (Number)
