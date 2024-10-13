import random
import pygame
pygame.init()
class Letter():
    def __init__(self,letter,pos):
        self.letter = letter
        self.displayedLetter = "_"
        self.position = pos
    def displayLetter(self,window):
        letter = font.render(self.displayedLetter, True, (0, 0, 0))
        window.blit(letter, (30+self.position*36, 450))

allWords,f = [],open("words.txt",'r')

for i in f.readlines():
    if 4 < len(i) < 10:
        allWords.append(i[:len(i)-1])

randomWord,letters = allWords[random.randint(0,len(allWords)-1)],[]
for i,l in enumerate(randomWord):
    t = Letter(l,i)
    letters.append(t)
window = pygame.display.set_mode((400, 500))
pygame.display.set_caption('HangMan')
images,running,color = [],True,(150,200,0)
for i in range(1,9):
    path = "images/" + str(i) + ".png"
    img = pygame.image.load(path)
    images.append(img)

def runGuess(letters,input):
    for letter in letters:
        if letter.letter == input:letter.displayedLetter = input

def displayLetters(letters,window):
    for letter in letters:letter.displayLetter(window)

def isWon(letters):
    for letter in letters:
        if letter.displayedLetter != letter.letter:return False
    return True

font,smallFont = pygame.font.SysFont("Arial", 36),pygame.font.SysFont("Arial",16)
alpha = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
guessNum,gameOver,currentInputLetter,guessedLetters= 0, False,"_",[]

while running:
    if not gameOver:window.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and not gameOver:
            if event.key == pygame.K_RETURN and not (currentInputLetter  in guessedLetters or currentInputLetter == "_"):
                runGuess(letters,currentInputLetter)
                if currentInputLetter not in randomWord:guessNum += 1
                guessedLetters.append(currentInputLetter)

                if isWon(letters):
                    window.blit(smallFont.render(f"You won and used {guessNum} guesses!", True, (0, 0, 0)), (20, 410))
                    gameOver = True
                if guessNum >= 8:
                    window.blit(smallFont.render(f"You lost and the word was {randomWord}!", True, (0, 0, 0)), (20, 410))
                    gameOver = True

            if chr(event.key).lower() in alpha:currentInputLetter = chr(event.key)

    currentLetterLetter = font.render(currentInputLetter, True, (0, 0, 0))
    displayLetters(letters,window)
    window.blit(currentLetterLetter, (70, 100))
    for i in range(guessNum):window.blit(images[i], (0, 0))
    pygame.display.flip()

