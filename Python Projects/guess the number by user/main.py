import random
def guess(x,y):
    random_number = random.randint(x,y)
    guess_number = None
    while guess_number!= random_number:
        guess_number = int(input(f"Enter the number between {x-1} and {y+1} : "))
        if guess_number < random_number:
            print("the guess is too low ,try again ")
        else:
            print("the guess is too high ,try again ")
    else:
        print(f"{guess_number} is the correct guess \n you won!! ")

while 1:
    
    if input("type play to start the game ").lower() == "play":
        a,b = input('enter the range of the guess ').strip.split()
        guess(int(a),int(b))
    if input("type restart to play again and type any other key to stop ").lower() == "restart":
        continue
    else:
        break

