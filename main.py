import random
import ascii

word_list = ['HYDROGEN', 'HELIUM', 'LITHIUM', 'BERYLLIUM', 'BORON', 'CARBON', 'NITROGEN', 'OXYGEN', 'FLUORINE', 'NEON', 'SODIUM', 'MAGNESIUM', 'ALUMINUM', 'SILICON', 'PHOSPHORUS', 'SULFUR', 'CHLORINE', 'ARGON', 'POTASSIUM', 'CALCIUM', 'SCANDIUM', 'TITANIUM', 'VANADIUM', 'CHROMIUM', 'MANGANESE', 'IRON', 'COBALT', 'NICKEL', 'COPPER', 'ZINC', 'GALLIUM', 'GERMANIUM', 'ARSENIC', 'SELENIUM', 'BROMIINE', 'KRYPTON', 'RUBIDIUM', 'STRONTIUM', 'YTTRIUM', 'ZIRCONIUM', 'NIOBIUM', 'MOLYBDENUM', 'TECHNETIUM', 'RUTHENIUM', 'RHODIUM', 'PALLADIUM', 'SILVER', 'CADMIUM,' 'INDIUM', 'TIN', 'ANTIMONY', 'TELLURIUM', 'IODINE', 'XENON', 'CESIUM', 'BARIUM', 'LANTHANUM', 'CERIUM', 'PRASEODYMIUM', 'NEODYMIUM', 'PROMETHIUM', 'SAMARIUM', 'EUROPIUM', 'GADOLINIUM', 'TERBIUM', 'DYSPROSIUM', 'HOLMIUM', 'ERBIUM', 'THULIUM', 'YTTERBIUM', 'LUTETIUM', 'HAFNIUM', 'TANTALUM', 'TUNGSTEN', 'RHENIUM', 'OSMIUM', 'IRDIUM', 'PLATINUM', 'GOLD', 'MERCURY', 'THALLIUM', 'LEAD', 'BISMUTH', 'POLONIUM', 'ASTATINE', 'RADON', 'FRANCIUM', 'ACTINIUM', 'THORIUM', 'PROTACTINIUM', 'URANIUM', 'NEPTUNIUM', 'PLUTONIUM', 'AMERICIUM', 'CURIUM', 'BERKELIUM', 'CALIFORNIUM', 'EINSTEINIUM', 'FERMIUM', 'MENDELEVIUM', 'NOBELIUM', 'LAWRENCIUM', 'RUTHERFORDIUM', 'DUBNIUM', 'SEABORGIUM', 'BOHRIUM', 'HASSIUM', 'MEITNERIUM']
#could add "hint" option, with specific clues about the words 
#could add "category" option so user could pick categories of words like "lab equipment" or "elements" or "famous figures"

word = random.choice(word_list)
chars_left = len(set(word))
lives_left = 6
guesses = []
word_blank = list(len(word)*[" _"])


def interface(lives_remaining, word_blank, guesses):
    print(ascii.ascii[lives_remaining])
    print(word_blank)
    print("You have already guessed the following: " + (', '.join(map(str, set(guesses)))))
    print(f"You have {lives_remaining} lives left")
    print("_____________________________________________")


def main():
    global chars_left
    global lives_left
    global word_blank
    print(ascii.ascii[6])
    print(''.join(map(str, word_blank)))
    print("\n")
    while lives_left > 0 and chars_left > 0:
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
    if lives_left == 0:
        print("You've run out of chances. Better luck next time!")
        print(f"If you're wondering, the word was {word}.")


print(ascii.ascii_intro)
print("\nHello! Welcome to the Periodic Table of Elements Hangman!\n\nHere are the rules:\n1. You get 6 lives before you die, if you guess an incorrect level, you lose a life\n2. If you guess the same letter twice, I'm going to judge you, but you don't lose a life\n3. If you guess a non-letter character, it counts against your lives AND I'm going to judge you\n4. Only guess one letter at a time; if you guess multiple letters at once, it'll count against your lives\n\nAnd that's pretty much it! Let's start the game! Have fun!\n\n_______________________________________________\n")
main()


# While loop
# Play_Again = input("Do you want to play again? (Yes/No)").upper()
# if Play_Again == "YES":
#     print("Awesome! Let's play again!")
#     main()
# elif Play_Again == "NO":
#     print("That's okay! Thanks for playing!")
#     exit()
# else: 
#     Play_Again = input("I don't understand, do you want to play again? Type \"Yes\" or \"No\"")




