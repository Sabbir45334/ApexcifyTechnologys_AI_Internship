# Import random module to allow computer to choose randomly
import random

# List of valid choices
choices = ["rock", "paper", "scissors"]

# Display game instructions
print("🎮 Rock-Paper-Scissors Game")
print("First player to reach 10 points wins!")
print("Type 'exit' anytime to quit\n")

# Outer loop (for restarting the game)
while True:

    # Reset scores at the start of each new game
    user_score = 0
    computer_score = 0

    # Game loop (runs until someone reaches 10 points)
    while user_score < 10 and computer_score < 10:

        # Take user input
        user = input("Enter rock, paper, or scissors: ").lower()

        # Exit option
        if user == "exit":
            print("\nGame exited 👋")
            break  # Exit inner loop

        # Validate input
        if user not in choices:
            print("❌ Invalid input! Try again.\n")
            continue  # Skip this round

        # Computer randomly selects
        computer = random.choice(choices)
        print("Computer chose:", computer)

        # Game logic
        if user == computer:
            print("🤝 It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        # Show score
        print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

    # If user exited early
    if user == "exit":
        print("Thanks for playing! 👋")
        break

    # Game finished (someone reached 10)
    print("🏁 GAME OVER")

    if user_score == 10:
        print("🎉 Congratulations! You are the WINNER!") 
    else:
        print("💻 Computer is the WINNER!")

    # Ask to restart
    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("Thanks for playing! 👋")
        break

    print("\n🔄 Restarting game...\n")
