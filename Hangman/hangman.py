import random
from words  import words
import string

def getValidWord(words):
    word = random.choice(words) # randomly choose something from the list
    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word.upper()   

def hangman():
    word = getValidWord(words)
    wordLetters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() # what the user has guess 
    
    lives = 6  

    # getting user input 
    while len(wordLetters) > 0 and lives >0 :
        # letters used 
        # " ".join(["a","b","cd"]) --> "a b cd"
        print("\nYou have ",lives," lives, you have used these letters: "," ".join(usedLetters))

        # what current word is (ie W-R D)
        wordList = [letter if letter in usedLetters else '-' for letter in word] 
        print('current word: ',' '.join(wordList))

        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet-usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives -=1 # takes away  life if wrong
                print("\nLetter ",userLetter," is not in word.")
        elif userLetter in usedLetters:
          print("You have already used that character.Please try again. ")
        else :
          print("Invalid character.Please try again.")  
    
    # gets here when len(wordLetters) == 0 Or when lives == 0 
    if lives == 0 :
        print("\nYou died, sorry.The word was",word)
    else:
       print("\nYou guess the word  ==>  ",word," !!")

hangman()