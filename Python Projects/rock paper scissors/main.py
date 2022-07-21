import random
def play():
    human = input("enter 'r' for rock ,'p' for paper and 's' for scissor ")
    computer = random.choice(['r','p','s'])
    if human == computer:
        print("its a tie ")
        play()
    elif decision(human,computer):
        print("HUMAN WON \n Humans are great")
    else:
        print("COMPUTER WON \n We are the future")
def decision(human,computer):
    if (human == 'p' and computer == 'r') or (human == 'r' and computer == 's') or (human == 's' and computer == 'p'):
        return True

play()