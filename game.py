import subprocess
import random
import  sys

while True:        
 print("<---------------------------Welcome to THE GAME------------------------------->")
 user_name = str(input("What is your name: "))
 print('Okay!' + user_name + ' lets play a game of rock, paper, scissors')
 print('Your choices are rock, paper, scissors')

 possible_actions = ['rock', 'paper', 'scissors']
 user_choices = str(input())

 computer_choice = random.choice(possible_actions)

 print(user_name + ' choice is '+ user_choices)
 print('Computer choice is ' +computer_choice)

 if user_choices == computer_choice:
    print(f"Both players selected {user_choices}. It's a tie!")
 elif user_choices == "rock":
    if computer_choice == "scissors":
        print("You win! because Rock smashes scissors.")
    else:
        print("You lose :( Paper covers rock!")
 elif user_choices == "paper":
    if computer_choice == "rock":
        print("You win! because Paper covers rock.")
    else:
        print("You lose :( Scissors cuts paper!")
 elif user_choices == "scissors":
    if computer_choice == "paper":
        print("You win! because Scissors cuts paper.")
    else:
        print("You lose :( Rock smashes scissors!")
 elif print("Invalid Input"):
     user_choices = "Invalid Input"
     break
 while True:     
        with open('gamedata.txt', 'a') as f:
            f.write('Player name: ' + user_name + "\n")        
            f.write('Player choice: ' + user_choices + "\n")
            f.write('Computer choice: ' + computer_choice + "\n")
            f.write("\n")
            break 
              
        
 print("<---------------------------Welcome to THE GAME------------------------------->")
 print("Want to paly again type'r'")
 print("Want to quit type 'x'")
 break

user_decision = str(input())
def main():
      python = sys.executable
      subprocess.call([python] + sys.argv)
      sys.exit()

if user_decision == 'r' or user_decision == 'Yes':
   print("Rebooting....")
   main()

if user_decision == 'x' or user_decision == 'No':
    print ("Bye, Bye")  
        