import random

print("""Welcome to Rock, Paper, Scissors!
    Rules:
    Rock beats Scissors
    Scissors beats Paper
    Paper beats Rock
    Let's play!""")

class RPS:
    def __init__(self):
        self.player_score = 0
        self.comp_score = 0

    def player_choice(self):
        while True:
            user_choice = input("Rock, Paper, or Scissors? ").lower()
            if user_choice in ["rock", "paper", "scissors"]:
                return user_choice
            else:
                print("Not a valid choice")

    def comp_choice(self):
        return random.choice(["rock", "paper", "scissors"])
    
    def rpsGame(self, player,comp):
        if player == comp:
            return "It's a tie!"
        elif (
            (player == "rock" and comp == "scissors") or
            (player == "scissors" and comp == "paper") or
            (player == "paper" and comp == "rock")
        ):
            self.player_score += 1
            return "You win!"
        else:
            self.comp_score += 1
            return "Computer wins!"

    def play(self):
            while True:
                player = self.player_choice()
                comp = self.comp_choice()
                result = self.rpsGame(player, comp)

                print(f"You chose {player}, computer chose {comp}. {result}")
                print(f"Player: {self.player_score} - Computer: {self.comp_score}")

                play_again = input("Do you want to play again? (yes/no) ").lower()
                if play_again == "no":
                    print("Thanks for playing! Final scores:")
                    print(f"Player: {self.player_score} - Computer: {self.comp_score}")
                    break

game = RPS()
while True:
    game.play()
    play_more = input("Do you want to play another game? (yes/no) ").lower()
    if play_more == "no":
        break