import sys
import random

def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3. \n\n")
        
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please choose 1, 2 or 3.")
            return play_guess_number()
        
        computerchoice = random.choice("123")

        print(f"{name}, you chose {playerchoice}.")
        print(f"I was thinking {computerchoice}. \n")

        playerchoice = int(playerchoice)
        computerchoice = int(computerchoice)

    def decide_winner():
        if player == computer:
            player +=1 
            print(f"{name}, You win!")
        else:
            return f"Sorry {name}, I was thinking {computerchoice}, better luck next time"
        
    game_result = decide_winner(player, computer)

    print(game_result)

    nonlocal game_count
    game_count += 1

    print(f"\nGame count: {game_count}")
    print(f"\n{name}'s win: {player_wins}")
    print(f"\nWinning percentage: {player_wins/game_count:.2%}")

    print(f"\n{name}would you like to play again?")

    while True:
        playagain = input("\nY for yes, \nQ for quit\n")
        if playagain.lower() not in ["y" or "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_guess_number()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        if __name__ == "__main__":
            sys.exit(f"Bye {name}!")
        else:
            return
        
    return play_guess_number

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized gaming experience."
    )

    parser.add_argument(
        '-n', '--name', metavar='name'
        required=True, help='The name of the person playing the game.'
    )
                  
    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()
        




