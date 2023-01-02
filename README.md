# Hangman

## Summary 
This project recreates the classic game "Hangman." Users have finite chances to guess the letters of a preselected secret word. Users can "win" the game by successfully guessing all the letters of the word, and "lose" the game by not guessing the correct letters in the allotted chances. I made this project to practice while loops, debugging, and independent coding and troubleshooting. 

## Example 
The game opens with a welcome image and basic instructions. A hangman block with underscores representing the letters in the secret word underneath it visually depict what spaces in the word are missing letters, and how many chances the player has left. 

<img width="771" alt="image" src="https://user-images.githubusercontent.com/97318084/210282448-840afcfe-fa2c-4794-9ac1-3adc02727c7b.png">

If the player selects the wrong letter, the program will add a body part to the hangman, and the text will inform the player that the letter was incorrect, as well as how many incorrect guesses are left. 

<img width="393" alt="image" src="https://user-images.githubusercontent.com/97318084/210282665-133048ae-0b0d-4c71-837f-bf4fa15a949b.png">

If the player selects the correct letter, the program will add the letter to the correct location(s) corresponding to the position of the letter in the word. 

<img width="352" alt="image" src="https://user-images.githubusercontent.com/97318084/210282745-bf0f3d27-0434-4c67-bffa-dc05d67fd287.png">

If the player wins, the program will congratulate the player and ask them if they want to play again.

<img width="518" alt="image" src="https://user-images.githubusercontent.com/97318084/210282813-58552367-149f-4efc-93f0-46064467b6ab.png">

If the player loses, the program will inform the player that the player has lost and ask if they want to play again. 

<img width="443" alt="image" src="https://user-images.githubusercontent.com/97318084/210282853-8cf5cb47-7382-41c6-90fc-cd10bf335b24.png">

If the player selects to play again, the game will restart. If the player selects to not play again, the game will terminate. If the player is unclear (does not select Yes/No), the program will tell the user that "[It doesn't} understand, do you want to play again? Type 'Yes' or 'No'." That prompt will loop until "yes" or "no" was selected. 

## To Do
- Add a while loop so that only single letter characters can be guessed. 
    - If a string of characters is guessed, count the guess against the player but inform the player that multi-character guesses do not work toward the secret word and that guesses must be one character at a time. 


## Credits
This project was inspired by Angela Yu's 100 Days of Code. 
