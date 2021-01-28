from string import ascii_uppercase as upper_case_alphabets
import random
from hangman_words import hangman_pics as picture
from hangman_words import words
import time

while True:
    word_to_guess = random.choice(words).upper()
    if " " in word_to_guess or "-" in word_to_guess:
        word_to_guess = random.choice(words).upper()
    else:
        break

lines = {}
count = 0
convert_word = {}
show_hangman = picture

""" def conversion(word, count) and 
    def show_conversion(word, converted_lines)
    are defined to check if the guess == word_pto_guess
"""
def conversion(word, count):
    for i in word:
        for position, character in enumerate(word):
            if character == i:
                convert_word[count] = i
        count += 1
    return convert_word

def show_conversion(word, converted_lines):
    if len(word) == 3:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2]
        return check_conversion

    elif len(word) == 4:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] +\
                           " " + converted_lines[3]
        return check_conversion

    elif len(word) == 5:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] +\
                           " " + converted_lines[3] + " " + converted_lines[4]
        return check_conversion

    elif len(word) == 6:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " +  converted_lines[5]
        return check_conversion

    elif len(word) == 7:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6]
        return check_conversion

    elif len(word) == 8:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6] + " " + converted_lines[7]
        return check_conversion

    elif len(word) == 9:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6] + " " + converted_lines[7] + " " + converted_lines[8]
        return check_conversion

    elif len(word) == 10:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6] + " " + converted_lines[7] + " " + converted_lines[8] + " " + \
                           converted_lines[9]
        return check_conversion

    elif len(word) == 11:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6] + " " + converted_lines[7] + " " + converted_lines[8] + " " + \
                           converted_lines[9] + " " + converted_lines[10]
        return check_conversion

    elif len(word) == 12:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6] + " " + converted_lines[7] + " " + converted_lines[8] + " " + \
                           converted_lines[9] + " " + converted_lines[10] + " " + converted_lines[11]
        return check_conversion

    elif len(word) == 13:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6] + " " + converted_lines[7] + " " + converted_lines[8] + " " + \
                           converted_lines[9] + " " + converted_lines[10] + " " + converted_lines[11] + " " + \
                           converted_lines[12]
        return check_conversion

    elif len(word) == 14:
        check_conversion = converted_lines[0] + " " + converted_lines[1] + " " + converted_lines[2] + " " + \
                           converted_lines[3] + " " + converted_lines[4] + " " + converted_lines[5] + " " + \
                           converted_lines[6] + " " + converted_lines[7] + " " + converted_lines[8] + " " + \
                           converted_lines[9] + " " + converted_lines[10] + " " + converted_lines[11] + " " + \
                           converted_lines[12] + " " + converted_lines[13]
        return check_conversion

def word_lines(word, count):
    for i in word:
        lines[count] = "_"
        count += 1
    return lines

# Show the line of word to guess (_ _ _ _ _ _ _ _)
def display_lines(word, get_lines):
    if len(word) == 3:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2]
        return check_display_line

    elif len(word) == 4:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3]
        return check_display_line

    elif len(word) == 5:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4]
        return check_display_line

    elif len(word) == 6:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5]
        return check_display_line

    elif len(word) == 7:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6]
        return check_display_line

    elif len(word) == 8:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6] + " " + get_lines[7]
        return check_display_line

    elif len(word) == 9:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6] + " " + get_lines[7] + \
                             " " + get_lines[8]
        return check_display_line

    elif len(word) == 10:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6] + " " + get_lines[7] + \
                             " " + get_lines[8] + " " + get_lines[9]
        return check_display_line

    elif len(word) == 11:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6] + " " + get_lines[7] + \
                             " " + get_lines[8] + " " + get_lines[9] + " " + get_lines[10]
        return check_display_line

    elif len(word) == 12:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6] + " " + get_lines[7] + \
                             " " + get_lines[8] + " " + get_lines[9] + " " + get_lines[10] + " " + get_lines[11]
        return check_display_line

    elif len(word) == 13:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6] + " " + get_lines[7] + \
                             " " + get_lines[8] + " " + get_lines[9] + " " + get_lines[10] + " " + get_lines[11] +\
                             " " + get_lines[12]
        return check_display_line

    elif len(word) == 14:
        check_display_line = get_lines[0] + " " + get_lines[1] + " " + get_lines[2] + " " + get_lines[3] +\
                             " " + get_lines[4] + " " + get_lines[5] + " " + get_lines[6] + " " + get_lines[7] + \
                             " " + get_lines[8] + " " + get_lines[9] + " " + get_lines[10] + " " + get_lines[11] +\
                             " " + get_lines[12] + " " + get_lines[13]
        return check_display_line


def hangman(word):
    new_convert_word = conversion(word_to_guess, count)
    get_show_conversion = show_conversion(word_to_guess, new_convert_word)

    new_line = word_lines(word_to_guess, count)
    show_display_lines = display_lines(word_to_guess, new_line)
    print(show_hangman[0])
    print("WORD = ", show_display_lines)
    incorrect_guess = set()
    correct_guess = set()
    # Ask the user for inputs
    # Ensure user input is an uppercase alphabet

    lives = 7
    limit = 7
    print(f"\nYou have {lives} lives left")
    while True:
        user_guess = input("Guess a letter: ").upper()
        if user_guess in upper_case_alphabets and user_guess in word:
            if user_guess in correct_guess:
                print("You have guessed this letter.")
                print("WORD = ", show_display_lines, "\n")
            else:
                correct_guess.add(user_guess)
                # Get position of user_guess and add to the dictionary
                for position, character in enumerate(word):
                    if character == user_guess:
                        new_line[position] = user_guess
                show_display_lines = display_lines(word_to_guess, new_line)
                print("WORD = ", show_display_lines, "\n")

        elif user_guess in upper_case_alphabets and user_guess not in word:
            if user_guess in incorrect_guess:
                print("You have guessed this incorrect letter!, try another alphabet.")
                show_display_lines = display_lines(word_to_guess, new_line)
                print("WORD = ", show_display_lines, "\n")
            else:
                lives -= 1
                print(f"{user_guess} is not in word to guess!, try another letter.")
                show_display_lines = display_lines(word_to_guess, new_line)
                print("WORD = ", show_display_lines, "\n")
                incorrect_guess.add(user_guess)
                if lives == 1:
                    print("\nThis is your last chance!")
                    print(show_hangman[6])
                elif lives > 1:
                    if lives == 2:
                        print(show_hangman[5])
                    elif lives == 3:
                        print(show_hangman[4])
                    elif lives == 4:
                        print(show_hangman[3])
                    elif lives == 5:
                        print(show_hangman[2])
                    elif lives == 6:
                        print(show_hangman[1])
                    print(f"\nYou have {lives} lives left")

        else:
            print(f"{user_guess} is an invalid input!")
            show_display_lines = display_lines(word_to_guess, new_line)
            print("WORD = ", show_display_lines, "\n")

        if show_display_lines == get_show_conversion:
            time.sleep(1)
            print(f"YOU WON! You guessed the word '{word}'")
            break

        if len(incorrect_guess) == limit:
            time.sleep(1)
            print(show_hangman[7])
            print(f"\nYOU ARE A DEAD MAN! The word was '{word}'")
            break

hangman(word_to_guess)