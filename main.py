import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print("Wszystkie dostępne elementy biblioteki (dir(colorama))")
print(dir(colorama))
print("\n")

print("Fore (kolory tekstu)")
print(dir(Fore))
print("\n")

print("Back (kolory tła)")
print(dir(Back))
print("\n")

print("Style (style tekstu)")
print(dir(Style))
print("\n")

print(" Przykładowe użycie")
print(Fore.RED + Style.BRIGHT + "➡ To jest jasny, czerwony tekst.")
print(Fore.GREEN + "➡ To jest zielony tekst.")
print(Back.YELLOW + "➡ Tekst z żółtym tłem.")
print(Fore.BLUE + Style.DIM + "➡ Niebieski, przyciemniony tekst.")
print(Style.RESET_ALL + "➡ Normalny tekst bez kolorów.\n")

# robilem to za pomoca youtuba, dla tego ze troche zapomnialem jak to robic
