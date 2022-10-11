import random
import colorama
from colorama import Fore
import sys
colorama.init(autoreset=True)
def random_word(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

official_word=random_word("wordlist.txt")
print(official_word)
official_word_list=list(official_word)
guess=0
guess_list=[]
check_list=[]
print("Please guess the word:")
for i in range(6):
    guess = input("\n")
    sys.stdout.write("\033[F")
    if len(guess)!=5:
        while len(guess)!=5:
            print("Word must be 5 letters long")
            guess = input("\n")
            sys.stdout.write("\033[F")
    guess_list=list(guess)
    if official_word!=guess:
        for i in range(0,5):
            if guess_list[i]==official_word_list[i]:
                check_list.append('g')
            else:
                if guess_list[i] in official_word_list:
                    check_list.append('y')
                else:
                    check_list.append('r')
    else:
        sys.stdout.write("\033[F")
        print(Fore.GREEN + official_word, end="")
        print("\nCongratulations! You guessed the word!")
        break
    for i in range(0,5):
        if check_list[i]=='g':
            print(Fore.GREEN+guess_list[i],end="")
        elif check_list[i]=='y':
            print(Fore.YELLOW+guess_list[i],end="")
        else:
            print(guess_list[i],end="")
    guess=0
    guess_list=[]
    check_list=[]