import random
import ascii
import word_bank

def interface(lives_remaining, word_blank, guesses):
    print(ascii.ascii[lives_remaining])
    print(word_blank)
    print("You have already guessed the following: " + (', '.join(map(str, set(guesses)))))
    print(f"You have {lives_remaining} lives left")
    print("_____________________________________________")


def main():
    global continue_game

    word = random.choice(word_bank.word_list)
    chars_left = len(set(word))
    lives_left = 6
    guesses = []
    word_blank = list(len(word)*[" _"])
    continue_game = True
    game_running = True
    
    print(ascii.ascii[6])
    
    while game_running:
        print(''.join(map(str, word_blank)))
        print("\n")
        guess = input("\nWhat letter do you guess? ").upper()
        
        if (guess not in set(guesses)) and (guess in list(word)):
            guesses.append(guess)
            print("\nGood guess!")
            chars_left -= 1
            for char in range(len(word)):
                if word[char] == guess: 
                    word_blank[char] = " " + guess

        elif guess in set(guesses) and guess in list(word):
            print("\nYou've already guessed that!")

        else:
            print("\nThat's not one of the letters... That's rough, buddy.")
            guesses.append(guess)
            lives_left -= 1

        word_blank_image = ''.join(map(str, word_blank))
        interface(lives_left, word_blank_image, guesses)

        if chars_left == 0:
            print("You Win!")
            game_running = False
        
        if lives_left == 0:
            print("You've run out of chances. Better luck next time!")
            print(f"If you're wondering, the word was {word}.")
            game_running = False
        

#### Primary Run ######

print(ascii.ascii_intro)
print("\nHello! Welcome to the Periodic Table of Elements Hangman!\n\nHere are the rules:\n1. You get 6 lives before you die, if you guess an incorrect letter, you lose a life\n2. If you guess the same letter twice, I'm going to judge you, but you don't lose a life\n3. If you guess a non-letter character, it counts against your lives AND I'm going to judge you\n4. Only guess one letter at a time; if you guess multiple letters at once, it'll count against your lives\n\nAnd that's pretty much it! Let's start the game! Have fun!\n\n_______________________________________________\n")

main()

while continue_game: 
    Play_Again = input("\n***\nThat was fun! Do you want to play again? (Yes/No)").upper()
    if Play_Again == "YES":
        print("Awesome! Let's play again!\n***\n\n")
        continue_game = False
        main()
    elif Play_Again == "NO":
        print("That's okay! Thanks for playing!")
        continue_game = False
    else: 
        Play_Again = input("I don't understand, do you want to play again? Type \"Yes\" or \"No\"  ").upper()