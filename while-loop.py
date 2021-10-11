import random #Imports the random module from Python Library

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number=random.randint(1,10) #Built-in function in the random module that randomly generates numbers
isGuessRight=False

while isGuessRight !=True:
    guess=input("Guess a number between 1 and 10: ")
    if int(guess)==number:
        #print("You guessed {}. That is correct! You win!".format(guess))
        print(f'You guessed {guess}. That is correct! You win!')
        isGuessRight=True
    else:
        print("You guessed {}. Sorry, that isn't it. Try again.".format(guess))