
import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
      |
     ===''', '''
  +---+
  O   |
 /|\\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\\  |
 / \\  |
     ===''', '''
  +---+
 [O   |
 /|\\  |
 / \\  |
     ===''', '''
  +---+
 [O]  |
 /|\\  |
 / \\  |
     ===''']
words = {'Colors': ('red orange yellow green blue indigo violet white black brown'.split(), 'The word is a color.A color is the answer.You must guess a color.'.split('.')),
'Shapes': ('square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(), 'The word is a geometric figure.A geometric figure is the answer.You must guess a geometric figure'.split('.')),
'Fruits': ('apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(), 'The word is a fruit.A fruit is the answer.You must guess a fruit'.split('.')),
'Animals': ('bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split(), 'The word is an animal.An animal is the answer.You must guess an animal'.split('.'))}

def getRandomWord(wordDict):
    ''' This function returns a random string from the passed dictionary of lists of strings, and the key also.'''
    
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey][0]) - 1)

    # Third, randomly select a clue from the key's tuple in the dictionary:
    clue = random.randint(0, len(wordDict[wordKey][1]) - 1)

    return [wordDict[wordKey][0][wordIndex], wordKey, wordDict[wordKey][1][clue]]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def getClue():
    #This function returns True if the player wants to get a clue, otherwise it returns False.
    print('Do you want to get a clue? You only have one clue. (yes or no)')
    return input().lower().startswith('y')

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
  print('Enter difficulty: E - Easy, M - Medium, H - Hard')
  difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet, secretClue = getRandomWord(words)
gameIsDone = False
clueDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if the player already got a clue.
        if not clueDone:
            if getClue():
                print('Clue: '+ secretClue)
                clueDone = True
        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            clueDone = False
            secretWord, secretSet, secretClue = getRandomWord(words)
        else:
            break

#Define la dificultad de los niveles en función de la cantidad
#de errores posibles.
#En algunos puntos no cumple con la PEP8, ya que esta recomienda
#limitar el numero de caracteres por linea a 79, y los comentarios
#a 72, cosa que no se cumple en este programa.