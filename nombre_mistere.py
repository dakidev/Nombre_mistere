from random import randint
from time import sleep
import colorama



def views_letter(text):
    for letter in text:
        print(letter, end='', flush=True)
        sleep(0.03)

counter = 5
start = randint(0, 100)
views_letter(colorama.Fore.BLUE + "*** Le Jeu du nomnbre mistère ***\n")

while counter > 0:
    if counter > 1:
        print(colorama.Fore.WHITE + f"Il vous reste {counter} essais.")
    else:
        print(colorama.Fore.WHITE + f"Il vous reste {counter} essai")
    user_input = input(colorama.Fore.WHITE +"Deviner le nombre : ")

    if not user_input.isdigit():
        views_letter(colorama.Fore.RED + "Veillez entrer un nombre valide\n")
        continue

    user_input = int(user_input)

    if user_input > start:
        views_letter(colorama.Fore.WHITE + f"Le nombre mistère est plus petit que {user_input} \n")
    elif user_input < start:
        views_letter(colorama.Fore.WHITE + f"Le nombre mistère est plus grand que {user_input} \n")
    else:
        break
    counter -= 1

if user_input == start:
    print(colorama.Fore.GREEN + "Bravo ! 👏👏👏")
    trying = 6 - counter
    if trying > 1:
        print(colorama.Fore.YELLOW + f"Vous avez trouve le nombre après {trying} essais")
    else:
        print(colorama.Fore.GREEN + f"Vous avez trouve le nombre après {trying} essai")
else:
    print(colorama.Fore.RED +"Dommage ! Le nombre mistère est : "+ colorama.Fore.GREEN + f"{start}")

print(colorama.Fore.WHITE +"\nFin du jeu !")
