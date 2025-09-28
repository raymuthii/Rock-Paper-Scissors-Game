import random # Import the random module to generate random numbers
print('============================================')
print('          Rock Paper Scissors Game          ')
print('============================================')
rock = 1
paper = 2
scissors = 3
print('1) Rock')
print('2) Paper')
print('3) Scissors')
player = int(input("Pick a number(1-3): "))
computer = random.randint(1, 3) # Assigns a random number between 1 and 3 to computer
print(f"Computer picked {computer}")
print(f"You picked {player}")

# Determine the winner using if-elif-else statements
if player == computer:
    print("It's a tie!")
elif (player == rock and computer == scissors) or (player == paper and computer == rock) or (player == scissors and computer == paper):
    print("You win!")
else:
    print("You lose!")

