import random

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/""")

word_list = ['handman', 'world', 'hello']

choosen_word = random.choice(word_list)

placeholder = ''
word_length = len(choosen_word)

print(f"Guess the {word_length} letter word.")

for i in range(word_length):
    placeholder += '_'
print(placeholder)

game_over = False
correct_letters = []

lives = 6

while not game_over:
    guess = input("Take a guess:").lower()
    print(guess)

    display = ''

    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter 
        else:
            display += '_'

    print(display)

    if guess in choosen_word:
        print("Correct guess")

    if guess not in choosen_word:
        lives -= 1
        print(f"Wrong guess, lives remaining: {lives}")
        if lives == 0:
            print("You lose")

    if '_' not in display:
        game_over = True
        print("You win!")