import time
a = True

while a == True:
    print("Hi! Ik ben Amber")
    jouwNaam = input("Wat is jouw naam? ")
    print ("Hey, "+ jouwNaam + ". Welkom!")
    time.sleep(1)
    print("Ik heb 3 vragen voor je:")

    time.sleep (1)
    print("1. Wat is mijn haarkleur?")
    print("A Bruin \nB Donker Rood \nC Paars \nD Donker Blond")
    
    antwoord1 = input("A, B, C of D ")

    if antwoord1 == "a" or antwoord1 == "A":
        print("Nope, als de kleur vervaagt word het wel bruin.")

    elif antwoord1 == "b" or antwoord1 == "B":
        print("Ja! Helaas vervaagt de kleur wel snel.")

    elif antwoord1 == "c" or antwoord1 == "C":
        print("Nope, maar wel in de buurt.")

    elif antwoord1 == "d" or antwoord1 == "D":
        print("Nee, dit is mijn echte haarkleur...")

    else:
        print("ik begrijp alleen maar a, b, c ofd als antwoord")


    time.sleep (2)
    print("Oke, nu vraag 2:")

    time.sleep (1)
    print("2. Wat is mijn favoriete eten?")
    print("A Pizza \nB Sushi \nC Lasagne \nD Stamppot andijvie")
    
    antwoord1 = input("A, B, C of D ")

    if antwoord1 == "a" or antwoord1 == "A":
        print("Nope, maar pizza is wel lekker!")

    elif antwoord1 == "b" or antwoord1 == "B":
        print("Niet mijn nummer 1, maar het is wel lekker.")

    elif antwoord1 == "c" or antwoord1 == "C":
        print("Jaa! En al helemaal als mijn moeder hem maakt.")

    elif antwoord1 == "d" or antwoord1 == "D":
        print("Nee, maar vind dit ook heel lekker.")

    else:
        print("ik begrijp alleen maar a, b, c ofd als antwoord")


    time.sleep (2)
    print("Oke, nu de laatste vraag:")

    time.sleep (1)
    print("3. Waar woon ik nu?")
    print("A Alkmaar \nB Haarlem \nC Spaarndam \nD Hoofddorp")
    
    antwoord1 = input("A, B, C of D ")

    if antwoord1 == "a" or antwoord1 == "A":
        print("Nee, maar ik ben hier wel geboren.")

    elif antwoord1 == "b" or antwoord1 == "B":
        print("Niet helemaal,ik heb hier wel 9 jaar gewoont.")

    elif antwoord1 == "c" or antwoord1 == "C":
        print("Ja, ik woon hier sinds 4 jaar.")

    elif antwoord1 == "d" or antwoord1 == "D":
        print("Nope!")

    else:
        print("ik begrijp alleen maar a, b, c ofd als antwoord")


    print("Yeay je hebt alle vragen gehad! Goed gedaan!")
    time.sleep(2)

    break
    

 
