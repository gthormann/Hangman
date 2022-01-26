import random


word_list = ['HYDROGEN', 'HELIUM', 'LITHIUM', 'BERYLLIUM', 'BORON', 'CARBON', 'NITROGEN', 'OXYGEN', 'FLUORINE', 'NEON', 'SODIUM', 'MAGNESIUM', 'ALUMINUM', 'SILICON', 'PHOSPHORUS', 'SULFUR', 'CHLORINE', 'ARGON', 'POTASSIUM', 'CALCIUM', 'SCANDIUM', 'TITANIUM', 'VANADIUM', 'CHROMIUM', 'MANGANESE', 'IRON', 'COBALT', 'NICKEL', 'COPPER', 'ZINC', 'GALLIUM', 'GERMANIUM', 'ARSENIC', 'SELENIUM', 'BROMIINE', 'KRYPTON', 'RUBIDIUM', 'STRONTIUM', 'YTTRIUM', 'ZIRCONIUM', 'NIOBIUM', 'MOLYBDENUM', 'TECHNETIUM', 'RUTHENIUM', 'RHODIUM', 'PALLADIUM', 'SILVER', 'CADMIUM,' 'INDIUM', 'TIN', 'ANTIMONY', 'TELLURIUM', 'IODINE', 'XENON', 'CESIUM', 'BARIUM', 'LANTHANUM', 'CERIUM', 'PRASEODYMIUM', 'NEODYMIUM', 'PROMETHIUM', 'SAMARIUM', 'EUROPIUM', 'GADOLINIUM', 'TERBIUM', 'DYSPROSIUM', 'HOLMIUM', 'ERBIUM', 'THULIUM', 'YTTERBIUM', 'LUTETIUM', 'HAFNIUM', 'TANTALUM', 'TUNGSTEN', 'RHENIUM', 'OSMIUM', 'IRDIUM', 'PLATINUM', 'GOLD', 'MERCURY', 'THALLIUM', 'LEAD', 'BISMUTH', 'POLONIUM', 'ASTATINE', 'RADON', 'FRANCIUM', 'ACTINIUM', 'THORIUM', 'PROTACTINIUM', 'URANIUM', 'NEPTUNIUM', 'PLUTONIUM', 'AMERICIUM', 'CURIUM', 'BERKELIUM', 'CALIFORNIUM', 'EINSTEINIUM', 'FERMIUM', 'MENDELEVIUM', 'NOBELIUM', 'LAWRENCIUM', 'RUTHERFORDIUM', 'DUBNIUM', 'SEABORGIUM', 'BOHRIUM', 'HASSIUM', 'MEITNERIUM']
#could add "hint" option, with specific clues about the words 
#could add "category" option so user could pick categories of words like "lab equipment" or "elements" or "famous figures"

lives_left = 6
word = random.choice(word_list)
incorrect_guesses = []
chars_left = len(word)
word_graphic = ("_")*len(word)
incorrect_guesses_string = str(", ".join(incorrect_guesses))

def turn_interface():
    global chars_left
    global lives_left
  #print corresponding ascii art from list corresponding to lives left
    print(word_graphic)
    print("You have guessed these letters: " + incorrect_guesses_string)
  #print(f"You have {lives_left} lives left.")
    guess = input("What letter would you like to guess? ").upper()
    for char in range(len(word)):
        if guess == word[char]:
            print(guess)
            print(word[char])
            print(char)
            word_graphic[char] = guess
            chars_left -=1
            return chars_left, word_graphic, lives_left 
            print("Good guess!")
    else:
        lives_left-=1
        incorrect_guesses.append(guess)
        print("That's rough, buddy")



########

print("Welcome to the Periodic Table of Elements Hangman! \n\nHere are the rules: \n1. \n\n")
print("Let's start the game! \n\n\n")

while lives_left>0 or chars_left>0:
    chars_left, word_graphic, lives_left = turn_interface()



