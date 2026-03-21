import random

print("Welcome to the Rock, Paper, Scissor Game.")

moves = ["rock", "paper", "scissor"]
AI_point = 0
player_point = 0

while True:
    print("\nWhat do you choose?")
    player_choice = input("Rock, Paper or Scissor: ").lower()

    if player_choice not in moves:
        print("Invalid choice! Try again.")
        continue

    AI_choice = random.choice(moves)
    print("AI's Choice:", AI_choice)

    if player_choice == AI_choice:
        print("It's a tie!")

    elif (
        (player_choice == "rock" and AI_choice == "scissor") or
        (player_choice == "paper" and AI_choice == "rock") or
        (player_choice == "scissor" and AI_choice == "paper")
    ):
        print("Player wins this round!")
        player_point += 1

    else:
        print("AI wins this round!")
        AI_point += 1

    print("AI point:", AI_point)
    print("Player point:", player_point)

    if player_point == 3:
        print("Congrats! You have won!")
        break
    elif AI_point == 3:
        print("You have lost. Better luck next time.")
        break

    print("Let's go another round!")
            
    
        
    
