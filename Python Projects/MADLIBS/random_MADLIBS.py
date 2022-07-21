from sample import example1,example2
import random

print("__name__:",__name__)
if __name__ == "__main__": 
    m = random.choice([example1,example2])  #random.choice  choose among the given list randomly
    
    m.madlib()