#!/usr/bin/env python3

pikachu={'First Appearance':'Pokemon Red and Green','Pokedex Number':25,'Origin':'Kanto','Designers':['Nishida','Sugimori'],'Type':'Electric'}

def main():
    pikachu["Cuteness"] = "overload"
    key_list = list(pikachu)
    i = 1
    for key in pikachu:
        print(f"{i}. {key}")
        i += 1

    choice = input("Choose a key: ")
    if (choice.isdigit() & int(choice) < len(key_list)):
        k = key_list[int(choice)-1]
        print(f"Pikachu's {k}: {pikachu[k]}")
    else:
        print("Sorry that is not a valid input")

main()
