import random

def name_to_number():
    while True:
        name = input("Rock, Spock, Paper, Lizard or Scissor?   ")
        name = name.lower()
        if name == "rock":
            return 0
        elif name == "spock":
            return 1
        elif name == "paper":
            return 2
        elif name == "lizard":
            return 3
        elif name == "scissor":
            return 4
        else:
            print("Please select between : Rock, Spock, Paper, Lizard or Scissor !!!!\n ")



def number_to_name(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == 4:
        return "Scissor"

def game(player1):
    player_choice = name_to_number()
    print(f"The Player 1 choose: {number_to_name(player_choice)}\n")

    computer_choice = random.randint(0, 4)
    print(f"Your Opponent choose: {number_to_name(computer_choice)}\n")

    who_win = (player_choice - computer_choice) % 5     #0: Tie.   1 or 2: Player 1 win       3 or 4: Computer Win
    if who_win == 0:
        print(f"It's a tie boyz !!!!\n")
    elif who_win == 1 or who_win == 2:
        print(f"Player 1 Win !!!!\n")
    elif who_win == 3 or who_win == 4:
        print(f"Your Opponent Win !!!!\n")

    again = input("Do you want to play again? y/n   ")
    if again.lower() == "y" or "yes":
        game(player1)
    else:
        print(f"Thanks for playing with us !!!")

game("player1")

