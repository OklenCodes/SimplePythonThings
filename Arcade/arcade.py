import sys
from rps import rps
from guess_number import guess_number

def play_game(name='PlayerOne'):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the arcade menu.")
        
        playerchoice = input(
            "\nPlease choose a game: \n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n"

        )
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please choose 1, 2 or x")
            return play_game(name)
            
        welcome_back = True 

        if playerchoice == 1:
            rock_paper_scissors = rps(name)
            rock_paper_scissors()

        elif playerchoice == 2:
            guess_number = guess_number()
            guess_number()

        else:
            print(f"\nSee you next time!\n")
            sys.exit(f"Bye {name}!")

if __name__ == main:
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides personalized gaming experience"
    )
        
    parser.add_argument(
        "-n", "--name", metavar='name',
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, Welcome to a new game")

    play_game(args.name)

