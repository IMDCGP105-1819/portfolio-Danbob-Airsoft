# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
Vowels = ["a" ,"e" ,"i" ,"o" ,"u"]
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secretlist= list(secret_word)
    e=0
    while e < len(secretlist):
        if secretlist[e] in letters_guessed:
            secretlist.remove(secretlist[e])
            e-=1
        e+=1
    if len(secretlist) == 0:
        return True
    else:
        return False
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secretlist = list(secret_word)
    guessedword = ""
    e=0
    while e < len(secretlist):
        if secretlist[e] in letters_guessed:
            guessedword += secretlist[e]
        else:
            guessedword += " _ "
        e +=1
    return guessedword
    # FILL IN YOUR CODE HERE AND DELETE "pass"




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    e=0
    Allletters = list(string.ascii_lowercase)
    while e < len(letters_guessed):
        if letters_guessed[e] in Allletters:
            Allletters.remove(letters_guessed[e])
        e +=1
    return Allletters
    # FILL IN YOUR CODE HERE AND DELETE "pass"

def finish (Number_Of_Guesses, secretlist):
    Letter_list = []
    x = 0
    while x < len(secretlist):
        if secretlist[x] not in Letter_list:
            Letter_list.append(secretlist[x])
        x += 1
    Score = Number_Of_Guesses * len(Letter_list)
    print ("Your Score was " + Score)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    Number_Of_Guesses = 50
    letters_guessed = []
    Guess = ""
    Warnings = 3
    print ("The word you are looking for contains " + str( len(secret_word)) + " letters")
    while Number_Of_Guesses > 1:
        print ("You have " + str(Number_Of_Guesses) + " Guesses left")
        print (get_available_letters(letters_guessed))
        Guess = input("Please input your guess ")
        print(Guess)
        if Guess.isalpha():
            if Guess in letters_guessed:
                if Warnings > 1:
                    Warnings -= 1
                    print ("You have already guessed that letter. " + str(Warnings) + " Warnings Remaining")
                else:
                    print ("You have attempted to enter the same letters too many times.")
                    Number_Of_Guesses -= 1
                    Warnings = 3
            elif Guess in list(secret_word):
                print ("That letter is in the word")
            else:
                print ("That letter is not in the word")
                if Guess in Vowels:
                    Number_Of_Guesses -= 2
                else:
                    Number_Of_Guesses -= 1
            letters_guessed += Guess
            Guessedword = get_guessed_word(secret_word, letters_guessed)
            print (Guessedword)
            Wordcheck = is_word_guessed(secret_word, letters_guessed)
            if Wordcheck:
                print ("You win! The word was " + secret_word)
                finish(Number_Of_Guesses, list(secret_word))
                break
            else:
                print ("The word is not yet complete. You have " + str(Number_Of_Guesses) + "Guesses left")

        else:
            if Warnings > 1:
                Warnings -= 1
                print ("That is not a letter you have " + str(Warnings) + " Warnings left")
            else:
                print ("You have entered too many invalid characters.")
                Number_Of_Guesses -= 1
                Warnings = 3

    else:
        print ("You did not guess the word in the guesses given. The word was " + str(secret_word))

    # FILL IN YOUR CODE HERE AND DELETE "pass"
secret_word = choose_word(wordlist)
hangman(secret_word)
