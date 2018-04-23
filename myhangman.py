import random

def drawRandomWord():
    """
    Function draws 1 random word from sowpods dictionary
    """
    with open("sowpods.txt", 'r') as file:
        listOfWords = file.readlines()
    wordsRange = random.randint(0, len(listOfWords)-1)
    drawnWord = listOfWords[wordsRange].strip()
    return drawnWord

secretWord = drawRandomWord()
lettersLeftToGuess = set(secretWord)
correctGuesses = set()
incorrectGuesses = set()
chancesUsed = 0

print("+ RIP Hangman +")
while (len(lettersLeftToGuess) > 0) and chancesUsed < 6:
    while True:
        letter = input("Type letter: ")
        if len(letter) == 1:
            break
        print("Please enter only one letter")
    guess = letter.upper().strip()

    if guess in correctGuesses or guess in incorrectGuesses:
        print("You already tried that letter")
        continue

    if guess in lettersLeftToGuess:
        lettersLeftToGuess.remove(guess)
        correctGuesses.add(guess)
    else:
        incorrectGuesses.add(guess)
        chancesUsed += 1

    output = []
    for letter in secretWord:
        if letter in correctGuesses:
            output.append(letter.upper())
        else:
            output.append("_")
    wordPrgoress = " ".join(output)
    print(wordPrgoress)

    chancesLeft = 6 - chancesUsed
    if chancesLeft > 1:
        print("You have " +str(int(chancesLeft))+ " guesses left")
    else:
        print("Thats your last chance")

if chancesUsed < 6:
    print("You did it! Your correctly guessed the word {}".format(secretWord))
else:
    print("Sorry you lost! Your word was {}".format(secretWord))
