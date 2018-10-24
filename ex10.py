Number = 1
for Number in range(1,100):
    if Number % 3 == 0 and Number % 5 == 0:
        print ("FizzBuzz")
    elif Number % 3 ==0:
        print ("Fizz")
    elif Number % 5 == 0:
        print ("Buzz")
    else:
        print (Number)
