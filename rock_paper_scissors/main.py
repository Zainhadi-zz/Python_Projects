import random
game_list = ['rock','paper','scissors']
computer = c= 0
command =p=0
print("score: computer"+ str(c)+"player"+str(p))
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("rock, paper, scissors, quit: ")
    if command == computer_choice:
        print("tie")
    elif command == 'rock':
        if computer_choice == 'scissors':
            print("player won!")
            p +=1
        else:
            print("computer won!")
            c +=1

