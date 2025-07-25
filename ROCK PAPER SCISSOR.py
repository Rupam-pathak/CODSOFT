import random

# Available choices
choices = ['rock', 'paper', 'scissors']

# Initialize scores
user_score = 0
computer_score = 0

#computers choice
def get_computer_choice():
    return random.choice(choices)

#USER CHOICE
def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid input. Please try again.")

#GAME DATA
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

def display_result(user, computer, result):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    
    if result == "tie":
        print("Result: It's a Tie!")
    elif result == "user":
        print("Result: You Win!")
    else:
        print("Result: Computer Wins!")

def play_again():
    """Ask user if they want to play again."""
    while True:
        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again in ['yes']:
            return True
        elif again in ['no']:
            return False
        else:
            print("Please answer with yes or no.")

# Main game loop
print("WELCOME TO ROCK, PAPER, SCISSOR GAME ")

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    # Update and display result
    if result == "user":
        user_score += 1
    elif result == "computer":
        computer_score += 1

    display_result(user_choice, computer_choice, result)

    # Show score
    print(f"\nScore => You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    if not play_again():
        print("\nThanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
