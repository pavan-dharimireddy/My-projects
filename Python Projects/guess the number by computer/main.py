import random
def guess(x,y):
    feedback = None
    while feedback != "c":
        guess_number = random.randint(x,y)
        print(f"my number is {guess_number}" )
        feedback = input(f"is my guess is high(h),low(l) or correct(c) ?? ")
        if feedback == 'h':
            y = guess_number   #like a binary search reduces the complexity to o(logN)
        elif feedback == 'l':
            x = guess_number
        else:
            feedback == 'c'
    else:
        print("HURRY!!, I WON ")
        print("I am proud to be a computer")

a,b = input("enter the range of number both inclusive ").strip().split()
guess(int(a),int(b))
            