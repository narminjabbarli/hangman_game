import random
import hangman_wordlist
import hangman_art

chosen_word = random.choice(hangman_wordlist.word_list)
word_length = len(chosen_word)
blanks = []
lives = 6
game_is_finished = False

for i in range(word_length):
    blanks += '_'

print(' '.join(blanks))
while not game_is_finished:
    guess = input('Guess a letter: ').lower()
        
    if guess in blanks:
        print(f'you have already guessed {guess}.')
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            blanks[position] = guess
            
    print(' '.join(blanks))
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -=1
        if lives == 0:
            game_is_finished = True
            print("You lose.")            

    if '_' not in blanks:
        game_is_finished = True
        print("You win.")
        
    print(hangman_art.stages[lives])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    