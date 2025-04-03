#Building a game where there are 2-4 players, if a player gets 1 after rolling the dice, that player's turn is over and his/her score becomes zero
#The game continues until
#a player achieve the max score let's say it is 20.

#Skeleton of this project:
#1)Take input of the number of players must be between 2-4
#2)A player rolls the dice
#3)If it is  1 then that player's turn is over, and then the next player rolls the dice until he/she gets 1
#4)we need to state the conditions for the win 
#5)we need announce the winner


#1
while True:
    pl_num=int(input("Enter the number of players(must be between 2-4): "))
    if pl_num<2 or pl_num>4:
        print("The number of players must be within the range provided")
    else:
        break


#2
import random
max_val=30
winner=None
player_score={}
for i in range(pl_num):
    player_score[f"Player {i+1}"]=0  #storing the score of the players

#3
while not winner:
    for i in player_score:
        print(f"{i}'s current score is {player_score[i]}")
        score=0

        while True:
             
                dice=random.randint(1,6)
                print(f"You rolled a {dice}")
                if dice==1:
                    print("Your turn is over") 
                    
                    break 
                else:
                    score+=dice
                    print(f" {i}'s current score is now {score}")

                    con=input("Would you like to continue?(y/n)").lower()
                    if con!="y":
                        print(f"Your score was {score}")
                        break

        player_score[i]+=score
        print(f"{i}'s total score is {player_score[i]}")
  
        #4
        if player_score[i]>=max_val:
            winner=i
            break

#5
print(f"Congrats {winner}!! You have won the game with a score of {player_score[i]} ")