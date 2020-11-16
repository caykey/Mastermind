import random
import time

print("\nWelcome to MASTERMIND!\n")
time.sleep(0.5)
print(
        "I will select four coloured pegs from the following colours:\n(R)ed, (O)range, (Y)ellow, (G)reen, (B)lue, (P)urple\n")
time.sleep(1)
print("Note that I am allowed to pick more than one of any colour.")
time.sleep(1)
print("Your mission is to guess the colours of the pegs I have chosen in the correct order.")
time.sleep(1)
print("You will type in your guess using the initial letter of the colours.")
print(
    "\nI will then tell you if there are pegs of the right colour and in the right place with a black peg,\nand pegs of the right colour in the wrong place with a white peg.")
time.sleep(1)
print("\nFor example:\n")
time.sleep(0.5)
print("I choose GBYY. On your first guess you try RBOG.")
time.sleep(1)
print(
    "So I then say Black White. You got a Black for the Blue in the right place, and a White for the Green in the wrong place.")
print("But you don't know what pegs Black and White refer to. You have to come up with a strategy to work it out!")
time.sleep(1)
print(
    "If you can guess the correct colours in the correct order, I will reply with Black Black Black Black and you will win the game!")
print("But you only have 10 guesses. If you can't do it in 10 guesses, then I win!")
time.sleep(1)
print("\nReady? Then lets go...")
time.sleep(1)

playing = True

while playing is True:

    playing = False

    pegs = random.choice("ROYGBP") + random.choice("ROYGBP") + random.choice("ROYGBP") + random.choice("ROYGBP")

    print("\nOK, I've chosen my colours.\n")
    print("Choose a pattern of 4 from, [R, O, Y, G, B, P]")
    guesses = 1

    while guesses <= 10:
        if guesses == 10:
            print("What's your last guess? ({} left)".format(10 - guesses))
        elif guesses == 1:
            print("What is your first guess? ({} left)".format(10 - guesses))
        elif guesses <= 9:
            print("What's your next guess? ({} left)".format(10 - guesses))
        guesses += 1
        choice = input("> ").upper()

        actualLetters = ['R', 'O', 'Y', 'G', 'B', 'P']

        while choice.isnumeric() is True:
            print("\nYou can't have a combination that contains numbers. [R, O, Y, G, B, P]")
            print("Please choose another combination that doesn't contain numbers.\n")
            choice = input("> ").upper()

        while len(choice) < 4 or len(choice) > 4:
            print("\nYou can't pick a combination that is less than or higher than 4.")
            print("Please choose another combination that is 4 characters.\n")
            choice = input("> ").upper()

        while (choice[0] not in actualLetters) or (choice[1] not in actualLetters) or (
                choice[2] not in actualLetters) or (choice[3] not in actualLetters):
            print("\nYou need to either use [R, O, Y, G, B, P]")
            print("Please re-enter a valid value.")
            choice = input("> ").upper()

        tmpPegs = pegs
        tmpChoice = choice
        black = 0
        white = 0

        if (pegs[0]) == (choice[0]):
            black += 1
            tmpPegs = tmpPegs[:0] + "1" + tmpPegs[1:]
            tmpChoice = tmpChoice[:0] + "2" + tmpChoice[1:]
        if (pegs[1]) == (choice[1]):
            black += 1
            tmpPegs = tmpPegs[:1] + "3" + tmpPegs[2:]
            tmpChoice = tmpChoice[:1] + "4" + tmpChoice[2:]
        if (pegs[2]) == (choice[2]):
            black += 1
            tmpPegs = tmpPegs[:2] + "5" + tmpPegs[3:]
            tmpChoice = tmpChoice[:2] + "6" + tmpChoice[3:]
        if (pegs[3]) == (choice[3]):
            black += 1
            tmpPegs = tmpPegs[:3] + "7" + tmpPegs[4:]
            tmpChoice = tmpChoice[:3] + "8" + tmpChoice[4:]

        if tmpChoice[0] in tmpPegs:
            white += 1
            tmpChoice = tmpChoice[:0] + "!" + tmpChoice[1:]
        if tmpChoice[1] in tmpPegs:
            white += 1
            tmpChoice = tmpChoice[:1] + "#" + tmpChoice[2:]
        if tmpChoice[2] in tmpPegs:
            white += 1
            tmpChoice = tmpChoice[:2] + "%" + tmpChoice[3:]
        if tmpChoice[3] in tmpPegs:
            white += 1
            tmpChoice = tmpChoice[:3] + "&" + tmpChoice[4:]

        print(choice + " = " + ("Black " * black) + ("White " * white))

        if choice == pegs:
            print("\nWell done! You got it. It took you {} guesses.".format(guesses))
            guesses = 11

        if guesses >= 11 and choice != pegs:
            print("\nYou're out of guesses, better luck next time!")
            print("My original choice was {}.".format(pegs))

    print("Play again? (Y or N)")
    playAgainChoice = input("> ").lower()

    Yeah = ['yes', 'ye', 'y', 'true']
    Nah = ['no', 'nah', 'n', 'false']

    while playAgainChoice not in Yeah + Nah:
        print("\nYou need to specify a valid answer.")
        print("Choose either 'yes' or 'no'.\n")
        playAgainChoice = input("> ").lower()

    if playAgainChoice in Yeah:
        print("Okay, playing again! :)")
        playing = True

    if playAgainChoice in Nah:
        print("Okay, I will not play again. :(")
