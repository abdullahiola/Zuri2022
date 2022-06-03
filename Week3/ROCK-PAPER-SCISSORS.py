import random

while True:
    player_input = input("""
        [ROCK-PAPER-SCISSORS CLI GAME]
        **** ENTER A CHOICE ***
        R FOR "ROCK"
        P FOR "PAPER"
        S FOR "SCISSORS"
    """).upper()
    options = ["R", "P", "S"]
    cpu_input = random.choice(options)

    if player_input == cpu_input:
        print(f"Both players selected {player_input}. It's a tie!")


    elif player_input == "R":
        if cpu_input == "S":
            print("""
                Player(ROCK):CPU(Scissors)
                "Rock beats scissors! Player wins!"
            """)
            
        else:
            print("""
                Player(ROCK):CPU(Paper)
                "Paper beats rock! You lose."
                CPU WINS!
            """)
            

    elif player_input == "P":
        if cpu_input == "R":
            print("""
                Player(Paper):CPU(Rock)
                "Paper covers rock! Player wins!"
            """)
            
        else:
            print("""
                Player(Paper):CPU(Scissors)
                "Scissors cuts paper! You lose."
                CPU WINS!
            """)
          

    elif player_input == "S":
        if cpu_input == "P":
            print("""
                Player(Scissors):CPU(Paper)
                "Scissors cuts paper! Player wins!"
            """)
            
        else:
            print("""
                Player(Scissors):CPU(Rock)
                "Rock smashes scissors! You lose."
                CPU WINS!
            """)
    
    else:
        print("ERROR! YOU DIDN'T SELECT A VALID CHOICE")
            
            
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


