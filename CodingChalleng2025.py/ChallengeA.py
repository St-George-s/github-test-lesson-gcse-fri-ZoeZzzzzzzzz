import random  #import random numbers file

num = random.randint(1,50)   #create variable num random number 1-50
print(num)
userGuess = input("Enter your guess(1-50): ")   #Ask user to input guess

while int(userGuess) != num:    #compare user guess to answer
    
    if int(userGuess) < num:    #comparing number to answer
        print("Too low! ") 
        userGuess = input("Enter another guess(1-50): ")   #Ask user to input guess again
    elif int(userGuess) > num:
        print("Too high!")
        userGuess = input("Enter another guess(1-50): ")   #Ask user to input guess
print("Good guess! You are correct!")   #congratulate
    
