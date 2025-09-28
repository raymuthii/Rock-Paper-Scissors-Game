import random # Import the random module to generate random numbers
print('============================================')
print('    Rock Paper Scissors Game With A Twist   ')
print('============================================')
rock = 1
paper = 2
scissors = 3
lizard = 4
spock = 5
print('1) Rock')
print('2) Paper')
print('3) Scissors')
print('4) Lizard')
print('5) Spock')
player = int(input("Pick a number(1-5): "))
computer = random.randint(1, 5) # Assigns a random number between 1 and 5 to computer
print(f"Computer picked {computer}")
print(f"You picked {player}")

# Determine the winner using if-elif-else statements
if player == computer:
    print("It's a tie!")
elif (player == rock and computer == scissors) or (player == paper and computer == rock) or (player == scissors and computer == paper) or (player == rock and computer == lizard) or (player == lizard and computer == spock) or (player == spock and computer == scissors) or (player == scissors and computer == lizard) or (player == lizard and computer == paper) or (player == paper and computer == spock):
    print("You win!")
else:
    print("You lose!")

