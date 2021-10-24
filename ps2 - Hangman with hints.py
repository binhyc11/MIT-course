import random
import string

WORDLIST_FILENAME = "words.txt"


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
wordlist = load_words()

def input_check (guess, letters_guessed):
    '''
    Input: guess, letters_guessed
    Check guess is a letter, is a vowel, is already guessed
    If not yet guessed, add to letters_guessed list
    Return: is_alpha, is_vowel, already_guessed, letters_guessed
    '''
    is_vowel = None
    already_guessed = None
    asterisk = None
    is_alpha = None
    if str.isalpha(guess) == True:  ### Check whether guess is a letter ###
        is_alpha = True
        if len (letters_guessed) > 0:
            if guess in letters_guessed:
                already_guessed = True
            if guess not in letters_guessed:  ### If not yet guessed, adding to letters_guessed ###
                letters_guessed.append(guess)
                already_guessed = False
        if len(letters_guessed) == 0:         ### If letters_guessed == 0, ie. starting the game, adding to letters_guessed ###
                letters_guessed.append(guess)
                already_guessed = False
        if guess in 'aeiou':        ### Check whether guess is a vowel ###
            is_vowel = True
        if guess not in 'aeiou':
            is_vowel = False
    if str.isalpha(guess) == False and guess != '*':
        is_alpha = False
    if str.isalpha(guess) == False and guess == '*':
        asterisk = True
    return is_alpha, is_vowel, already_guessed, letters_guessed, asterisk

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            guessed_word += '_ '
        else:
            guessed_word += secret_word[i]
    return guessed_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lowercase = string.ascii_lowercase
    available_letters = ''
    for i in lowercase:
        if i not in letters_guessed:
            available_letters += i
    return available_letters
    
def unique_letter (secret_word):
    '''
    Input: secret_word
    Return: number of unique letters, unique letters list
    '''
    number_unique = 0
    unique = []
    for i in string.ascii_lowercase:
        if i in secret_word:
            number_unique += 1
            unique.append(i)
    return number_unique, unique

def remaining (is_alpha, is_vowel, already_guessed, guessed_word, remaining_guesses, remaining_warnings, guess, secret_word):
    '''
    Calculate remaining guesses and warnings
    '''
    if is_alpha == False:
        if remaining_warnings == 0:
            remaining_guesses -= 1
        if remaining_warnings > 0:
            remaining_warnings -= 1
    if is_alpha == True:
        if already_guessed == True:
            if remaining_warnings == 0:
                remaining_guesses -= 1
            if remaining_warnings > 0:
                remaining_warnings -= 1
        if (is_vowel == True) and (guess not in secret_word) and (already_guessed == False):
            remaining_guesses -= 2
        if (is_vowel == False) and (guess not in secret_word) and (already_guessed == False):
            remaining_guesses -= 1
    return remaining_guesses, remaining_warnings

def print_statement (remaining_guesses, remaining_warnings, available_letters):
    '''
    Print remaining_guesses, remaining_warnings left; Available_letters
    '''
    if remaining_warnings > 1 and remaining_guesses > 1 :
        print ('You have', remaining_guesses, 'guesses and', remaining_warnings, 'warnings left.\n')
    if remaining_warnings <= 1 and remaining_guesses > 1:
        print ('You have', remaining_guesses, 'guesses and', remaining_warnings ,'warning left.\n')
    if remaining_guesses <= 1 and remaining_warnings <= 1:
        print ('You have', remaining_guesses, 'guess and', remaining_warnings ,'warning left.\n')
    if remaining_guesses <= 1 and remaining_warnings > 1:
        print ('You have', remaining_guesses, 'guess and', remaining_warnings ,'warning left.\n')
    if remaining_guesses > 0:
        print ('Available letters:', available_letters)
    
def print_input_check ( is_alpha, is_vowel, already_guessed, guessed_word, guess, secret_word, asterisk):
    if is_alpha == False:
        print ('\nOops! That is not a valid letter.', guessed_word, "\n -----------\n")
    if already_guessed == True:
        print ("\nOops! You've already guessed that letter.", guessed_word, "\n -----------\n")
    if guess in secret_word and already_guessed == False :
        print ('\nGood guess:', guessed_word, "\n -----------\n")
    if guess not in secret_word and is_alpha == True and already_guessed == False :
        print ('\nOops! That letter is not in my word.', guessed_word, "\n -----------\n")
    if asterisk == True:
        print ('Possible word matches are: ', show_possible_matches(guessed_word), "\n -----------\n")

def is_word_guessed(letters_guessed, unique):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    if set(unique) <= set(letters_guessed):  ### check if secret_word is a subset of letters_guessed ###
        flag = True
    else:
        flag = False
    return flag

def match_with_gaps(guessed_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    check = []
    draft = guessed_word.replace(' ','')
    if len(draft) != len (other_word):
        check.append('F')
    if len(draft) == len (other_word):
        for i in range (len(draft)):
            if str.isalpha(draft[i]) == True and draft[i] == other_word [i]:
                 check.append('T')
            if str.isalpha(draft[i]) == True and draft[i] != other_word [i]:
                 check.append('F')
    if 'F' not in check:
        match = True
    if 'F' in check:
        match = False
    return match            

def show_possible_matches(guessed_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    draft = guessed_word.replace(' ','')
    possible_words = []
    for word in wordlist:
        if match_with_gaps(guessed_word, word) == True:
            possible_words.append(word)
    return possible_words


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    remaining_guesses = 6
    remaining_warnings = 3
    letters_guessed = []
    number_unique, unique = unique_letter (secret_word)
    
    print ('Welcome to the game Hangman!\n\nI am thinking of a word that is', len(secret_word) ,'letters long. \n -----------')
    print ('You have 6 guesses and 3 warnings left.\n\nAvailable letters: abcdefghijklmnopqrstuvwxyz\n')
    
    
    while remaining_guesses > 0 and is_word_guessed(letters_guessed, unique) == False:
        guess = str.lower (input ('Please guess a letter: ',))
        is_alpha, is_vowel, already_guessed, letters_guessed, asterisk = input_check (guess, letters_guessed)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        available_letters = get_available_letters(letters_guessed)
        remaining_guesses, remaining_warnings = remaining (is_alpha, is_vowel, already_guessed, guessed_word, remaining_guesses, remaining_warnings, guess, secret_word)
        print_input_check ( is_alpha, is_vowel, already_guessed, guessed_word, guess, secret_word, asterisk)
        print_statement (remaining_guesses, remaining_warnings, available_letters)

    
    ### Game ends ###
    if remaining_guesses <= 0:
        print ('Sorry, you ran out of guesses. The word was else:', secret_word)
    if is_word_guessed(letters_guessed, unique) == True:
        score = remaining_guesses * number_unique
        print ('Congratulations, you won! \n Your total score for this game is:', score)


    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)