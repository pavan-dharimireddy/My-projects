from random_words import words
import random
import string


def valid_word(words):
    temp_word = random.choice(words)
    # print(word)
    # do not type this line while '-' or '_' in current_word: because its makes process too long
    while '-' in temp_word or '_' in temp_word:
        temp_word = random.choice(words)

    return temp_word.lower()


def play_hangman(words):
    current_word = valid_word(words)
    word_letters = set(current_word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = len(current_word)*2 + 3
    print("\n length of the word : ",len(current_word))

    while len(word_letters) > 0 and lives >0:
        print("\n till now you have used this letters : ",' '.join(used_letters)) #' '.join(['a','b','abc'])--> 'a b abc'

        guessed_word_list = [letter  if letter in used_letters else "-" for letter in current_word ]  #revealing the word 
        #example, current status of the word = p-v-n
        
        print("\n you have lives remaining : ",lives," , and  current status of the word : ",' '.join(guessed_word_list))
        user_letter = input("\n Enter your letter : ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print(f"\n entered letter '{user_letter}' is not in the guessing word ")
                lives -= 1
        elif user_letter in used_letters:
            print("\n you already used this letter --", user_letter)
        else:
            print("\n you entered a invalid character,try again")
        print("$"*100)
    if lives> 0:
        print("\n HURRAY,you won the game")
        print("\n word = ",current_word)
    else:
        print("\n you lost the game")
        print("word = ",current_word)

play_hangman(words)
