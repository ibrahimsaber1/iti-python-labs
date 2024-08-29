import random

fruits = [
  "Apple", "Banana", "Orange", "Strawberry", "Grape", "Pineapple", "Mango",
  "Blueberry", "Watermelon", "Kiwi", "Peach", "Cherry", "Pomegranate",
  "Cantaloupe", "Papaya", "Blackberry", "Raspberry", "Lemon", "Lime",
  "Coconut", "Grapefruit", "Plum", "Apricot", "Fig", "Guava", "Jackfruit",
  "Lychee", "Mandarin", "Nectarine", "Passionfruit", "Pear", "Persimmon",
  "Quince", "Tangerine", "Dragonfruit", "Durian", "Starfruit", "Mulberry",
  "Honeydew", "Cranberry", "Date", "Elderberry", "Gooseberry", "Acai",
  "Boysenberry", "Currant", "Jujube", "Longan", "Mangosteen", "Olive",
  "Plantain"]



while True :
    
    word = random.choice(fruits).lower()
    chances = len(word)+2 
    guess_letters = list("_" * len(word))
    guess_letters_str = " ".join(guess_letters)
    count = 0

    print("*"*70)
    print("Welcom to the Hang Man Game :)")
    print("Guess the word! HINT: word is a name of a fruit")
    print("*"*70, end="\n")
    print(word)
    print(f"{guess_letters_str}  ==> | You have {chances } chances to solve it |")
    print("*"*70)



    for j in range(chances): 
        letter = input("Guess a single letter: ").lower()
        count = count + 1

        if not letter.isalpha():
            print("please enter a letters only !!!")
            print(f"{' '.join(guess_letters)} ==> | You have {chances - count} chances to solve it |\n{'*'*70}")
            continue

        if len(letter) > 1:
            print("please enter a single letter only !!!")
            print(f"{' '.join(guess_letters)} ==> | You have {chances - count} chances to solve it |\n{'*'*70}")
            continue

        if len(letter) == 0:
            print("please enter at least a single letter !!!")
            print(f"{' '.join(guess_letters)} ==> | You have {chances - count} chances to solve it |\n{'*'*70}")
            continue

        if letter in guess_letters:
            print("you guess this letter already !!!")
            print(f"{' '.join(guess_letters)} ==> | You have {chances - count} chances to solve it |\n{'*'*70}")
            continue

        for i in range(len(word)):
            if word[i] == letter:
                guess_letters[i] = letter
        
        print(f"{' '.join(guess_letters)} ==> | You have {chances - count} chances to solve it |\n{'*'*70}")
        if "".join(guess_letters) == word:
            break

    if "".join(guess_letters) != word:
    # lose-case
        print(f"You lost! Try again..\nThe word was {word}")
    else:
    # win-case
        print(f"you guessed the correct word: {word}\nin {count} chances")

    answer = input("want to play again? yes / no ").lower()
    if answer == 'no' or answer == 'n':
        print("Bye! Bye!")
        break
    

