import random 
 
print("Number guessing game") 
 # randint function to generate the random number between 1 to 9 
number = random.randint(1, 9) 
 # number of chances to be given to the user to guess the number 
 # # or it is the inputs given by user into input box here number of chances are 5 
chances = 0 
 
print("Guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input('Enter your guess '))
    if guess == number:
        print('Congratulations You Have Won')
        break
    elif guess < number:
        print('Your guess was too low, enter a higher number')
    else:
        print('Your guess was too high, enter a lower number')

    chances += 1

if not chances < 5:
    print('You Lose, the number is ', number)
