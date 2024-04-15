import random
# Python's Random Game Night

# Create a guessing game via random.choice and user input
# Initialize a list of colors
# Initialize an input variable
 
colorList = ["red", "blue", "green", "yellow"]
color = random.choice(colorList)


print("""Can you match the color? Type either:
        red
        blue
        green
        yellow"""
      )


while(True):
    userGuess = input().lower()
    if userGuess == color:
        print("You guessed right!")
        break

    print("Wrong guess!")
