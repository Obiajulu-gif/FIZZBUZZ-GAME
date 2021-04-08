
#first it will go over in range of 1 to 100
# n is the varable been assigned to the range value
for n in range (1, 101):
    
    if n % 3 == 0 and n % 5 == 0: # it will check if a number is divisible by 3 and 5
        print ("FizzBuzz")
    elif n % 3 == 0:        #it will check if a number is divisible by 3
        print ("Buzz")
    elif n % 5 == 0:        #it will check if a number is divisivle by 5
        print ("Fizz")
    else:                   #it will check if others is false else it will print it's number in the loop
        print (n)
  
                   #NOTE
#in this code we observe the order in which python read code
# i.e. it start from top to buttom
# so if one of the above condition is correct it stops there
#and it no read the other parts
# so it advisiable to start ur if statement with the one that have double condition
# i.e. the one that might bear "and / or " logic in it
