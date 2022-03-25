# coding a rock paper scissors game! fun!

import random

def rock_paper_scissors():
    name = input("What is your name? ")
    
    game_count = {name: 0,
                "computer": 0,
        }

    def play():
        prompt1 = "Would you like to play rock paper scissors? Choose your fighter (rock, paper, or scissors)? "
        prompt2 = 'Do you want to play again (y/n)? '
        computer_list = ['rock', 'paper', 'scissors']
        message = {
            "tie" : ["boring, it's a tie!", "tie, You guys both suck!", "it's an old fashion draw"],
            "won" : ["yasss Queen, it's a win for you henay!", "you're awesome! Great Win", "you won! The computer didn't see it coming"], 
            "lost" : ["boo, you lost", "better luck next time sparky", "you lose, bitch"]
        }
    
        while True:
            game_c = input(prompt1) 
            computer_c = random.choice(computer_list)
            if game_c == computer_c:
                print(f"Computer selected {computer_c}, {random.choice(message['tie'])}")
                end_game = input(prompt2)
                if end_game == 'y':
                    continue
                if end_game == 'n':
                    break
                
            elif (game_c == 'rock' and computer_c == 'scissors') or (game_c == 'scissors' and computer_c == 'paper') or (game_c == 'paper' and computer_c == 'rock'):
                print(f"Computer selected {computer_c}, {random.choice(message['won'])}")
                game_count[name] += 1
                end_game = input(prompt2)
                if end_game == 'y':
                    continue
                if end_game == 'n':
                    break

            elif (game_c == 'rock' and computer_c == 'paper') or (game_c == 'scissors' and computer_c == 'rock') or (game_c == 'paper' and computer_c == 'scissors'):
                print(f"Computer selected {computer_c}, {random.choice(message['lost'])}")
                game_count["computer"] += 1
                end_game = input(prompt2)
                if end_game == 'y':
                    continue
                if end_game == 'n':
                    break
                    
            else:
                print("Invalid entry.")
                continue
               
        
        playing = True
        while playing:    
            prompt3 = 'You sure you want to quit (q) or do you want to play again (y) or show your score (s)? '
            end_game = input(prompt3)
            
            if end_game.lower() == 'y':
                play()

            elif end_game.lower() == 'q':
                print("Goodbye!")
                playing = False
            elif end_game.lower() == 's':
                print(game_count)
                end_game2 = input('Do you want to play again (y/n)? ')
                if end_game2.lower() == 'y':
                    play()
                elif end_game2.lower() == 'n':
                    print("Goodbye!")
                    playing = False
                else:
                    print("Invalid entry.")
                
            else:
                print("Invalid entry.")
            


    play()

    # return play


rock_paper_scissors()


