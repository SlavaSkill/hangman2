from gameplay.game import Game
import random 
from nltk import word_tokenize
#split varejam pameginat

with open('data/words.txt', 'r', encoding='utf-8') as file:
    words = file.read()
    words = word_tokenize(words)
#join no saraksta uz simbola virkni
#Sakuma cik burtus musu varda?

while True:
    # Randomize each game
    random.shuffle(words)
    word = words.pop()
    game = Game(word)
    #game = Game(random.choice(words))
    game.play()
    
    exit_ = input('do you want to exit? y/n: ')
    if exit_ == 'y':
        break
    else:
        continue
