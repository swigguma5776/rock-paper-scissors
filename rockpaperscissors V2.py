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
            "tie" : ["Boring, it's a tie!", "Tie, You guys both suck!", "It's an old fashion draw"],
            "won" : ["Yasss Queen, it's a win for you henay!", "You're awesome! Great Win", "You won! The computer didn't see it coming"], 
            "lost" : ["Boo, you lost", "Better luck next time sparky", "You lose, bitch"]
        }
        
        
        
        game_c = input(prompt1) 
        while True:
            
            if game_c == random.choice(computer_list):
                print(random.choice(message['tie']))
                end_game = input(prompt2)
                if end_game == 'y':
                    game_c = input(prompt1)
                if end_game == 'n':
                    break
                
            elif game_c == 'rock' and random.choice(computer_list) == 'scissors':
                print(random.choice(message['won']))
                game_count[name] += 1
                end_game = input(prompt2)
                if end_game == 'y':
                    game_c = input(prompt1)
                if end_game == 'n':
                    break
                    
            elif game_c == 'scissors' and random.choice(computer_list) == 'paper':
                print(random.choice(message['won']))
                game_count[name] += 1
                end_game = input(prompt2)
                if end_game == 'y':
                    game_c = input(prompt1)
                if end_game == 'n':
                    break
                            
            elif game_c == 'paper' and random.choice(computer_list) == 'rock':
                print(random.choice(message['won']))
                game_count[name] += 1
                end_game = input(prompt2)
                if end_game == 'y':
                    game_c = input(prompt1)
                if end_game == 'n':
                    break
                    
            else:
                print(random.choice(message['lost']))
                game_count["computer"] += 1
                end_game = input(prompt2)
                if end_game == 'y':
                    game_c = input(prompt1)
                if end_game == 'n':
                    break

        # while True:    
        end_game = input('You sure you want to quit (q) or do you want to play again (y) or show your score (s)? ')
        if end_game.lower() == 'y':
            play()

        elif end_game.lower() == 'q':
            return "Goodbye!"
        elif end_game.lower() == 's':
            print(game_count)
            end_game2 = input('Do you want to play again (y/n)? ')
            if end_game2.lower() == 'y':
                   play()
            elif end_game2.lower() == 'n':
                   return "Goodbye!"
            else:
               print("Invalid entry.")
        else:
            print("Invalid entry.")


    print(play())

    return play 


print(rock_paper_scissors())


