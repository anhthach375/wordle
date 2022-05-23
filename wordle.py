import random 

def chooseHiddenWord(worlList:list) -> str:
    # Choose a word randomly from the passed list and return it.
    randomWord:str = worlList[random.randint(0, len(worlList)-1)]
    return randomWord

def isValidWord(word:str, validWords:list) -> bool:
# Returns True if the given word is in the list of valid words.
    validWords = readFileToList('scrabble5.txt')
    for i in validWords:
        if word == i:
            return True
    return False

def readFileToList(filePath:str) -> list:
    with open( filePath, 'r') as reader:
        # for each line of the file we're reading
        fileContents:list = []
        for line in reader:
            # use the strip method to remove any extra whitespace at the
            # beginning or end of the line.  In this case, the only thing
            # that is removed is the "return" character at the end of the line
            lineContents = line.strip()
            fileContents.append(lineContents)
    # placeholder - return the empty list for now
    return fileContents

def playWordle() -> bool:
# read the common words list from "common5.txt" -- this is where the hidden words are pulled from
    commonWords:list = readFileToList('common5.txt')
# read the valid words list from "scrabble5.txt" -- this is the list to check a user's guess against
    validWords:list = readFileToList('scrabble5.txt')
# choose a hidden 5-letter word from the common words list
    hiddenWord:str = chooseHiddenWord(commonWords)
    # print(hiddenWord)
    # print(f'ROUND 1!')
    # result:bool = playRound(hiddenWord, validWords)
    for round in range(1,7):
            print(f'ROUND {round}!')
            result:bool = playRound(hiddenWord, validWords)
            if result == True:
                print(f'Yes, the word was {hiddenWord}.')
                return True 
    print(f'The word was {hiddenWord}.')
    return False

def playRound(hiddenWord:str, validWords:list) -> bool:
# # Given the hiddenWord and current guesses and clues, play a round of the game. Prompt the user for their guess. If the user enters an invalid word, then "....." is substituted as a default. Returns True if they guessed the hiddenWord and False otherwise.
    validWords = readFileToList('scrabble5.txt')
    guessWord = input('What is your guess? ')
    if not isValidWord(guessWord, validWords):
        guessWord = "....."
    print(guessWord)
    clueIs:str = createClue(hiddenWord, guessWord)
    return gameWon(clueIs)
     
    
def gameWon(clue:str) -> bool:
# # Given a clue, check if the game has been won; return True if it has, False otherwise.
        if clue == 'â™¥â™¥â™¥â™¥â™¥':
            return True
        else:
            return False
    
def createClue(hiddenWord:str, guess:str) -> str:
# Initialize a clueList variable of type list to hold 5 "?" values (this will help us know which entries we haven't finalized)
    clueList:list = ['?', '?', '?', '?', '?']
# In order to build the clue, we'll need to match letter's in the player's guess against letters in the hidden word. We'll do this by maintaining two lists.
# We will track the unmatched letters of the hidden word
    unmatchedHiddenLetters:list = list(hiddenWord)
# We will track the unmatched letters of the guess. Initialize it to the user's guess using the list function as above.
    unmatchedGuessLetters:list = list(guess)
# First, update the three lists to reflect completely right/wrong guess values by invoking    updateClueForRightAndWrong
    updateClueForRightAndWrong(clueList, unmatchedHiddenLetters, unmatchedGuessLetters)
# Then, update the lists to match guessed letters in the hidden word (not yet matched) with the first occurrence in the guess by invoking updateClueForPartialMatches
    updateClueForPartialMatches(clueList, unmatchedHiddenLetters, unmatchedGuessLetters)
# Finally, clear out the unmatched guess letters (these are additional occurrences of letters in the hidden word) by invoking updateClueForMismatches
    updateClueForMismatches(clueList)
    clueAsString:str = "".join(clueList)
    print(clueAsString)
    return clueAsString
    
def updateClueForRightAndWrong(clue:list, unmatchedHiddenLetters:list, unmatchedGuessLetters:list) -> None:
# Walk the guess letters and hidden letters in parallel by looping over the index values 0,...,4
    for i in range(0,5):
# If there is a match (correct letter in the correct spot), update the clue to be a "â™¥"
        if unmatchedHiddenLetters[i] == unmatchedGuessLetters[i]:
            clue[i] = 'â™¥'         
# update the remainingHiddenLetters and remainingGuessLetters lists to both hold "" ("clear out" the letter from consideration)
            unmatchedHiddenLetters[i] = ""
            unmatchedGuessLetters[i] = ""
# Otherwise if the letter is not matchable (which is when it is not in the list of unmatched hidden letters)
        elif unmatchedGuessLetters[i] not in unmatchedHiddenLetters:
            clue[i] = '_'

def updateClueForPartialMatches(clue:list, unmatchedHiddenLetters:list, unmatchedGuessLetters:list) ->  None:
# iterate over the hidden letters to find partial matches
    for hiddenLetter in unmatchedHiddenLetters:
# if it's a real letter (not "") and it's a letter that was guessed (but wasn't matched)
        if hiddenLetter != "" and hiddenLetter in unmatchedGuessLetters and unmatchedGuessLetters.index(hiddenLetter) != unmatchedHiddenLetters.index(hiddenLetter):
# find the index of the first occurrence in the unmatched guess letters (here is the code, since you may not be familiar with the string method index):
# update the clue to have a "â™¡" there
            firstIndex:int = unmatchedGuessLetters.index(hiddenLetter)
            clue[firstIndex] = 'â™¡'
# update the unmatchedGuessLetters to "" since we've matched it
            unmatchedGuessLetters[firstIndex] = ""
# if hiddenLetter not in unmatchedGuessLetters:
        
def updateClueForMismatches(clue:list) -> None:
# Change all "?" to "_" 
    for i in range(0,5):
        if clue[i] == '?':
            clue[i] = '_'

def main():
    result:bool = playWordle()
    if result == True:
        print('Congratulations, you won!')
    else:
        print('Too bad, you lost.')

if __name__ == "__main__":
    main()