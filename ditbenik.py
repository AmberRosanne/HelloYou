

print("Dit is mijn 'dit ben ik' text game")
print("Hi! Ik ben Amber")
jouwNaam = input("Wat is jouw naam? ")

print ("Hey, "+ jouwNaam + ". Welkom!")
print("1. Wat is mijn haarkleur?")
print("A Bruin \nB Donker Rood \nC Paars \nD Donker Blond")

antwoord1 = input("a b c of d ")
print("Jouw antwoord is dus " + antwoord1)


if antwoord1 == "a" or antwoord1 == "A":
    print("Nope, als de kleur vervaagt word het wel bruin")

if antwoord1 == "b" or antwoord1 == "B":
    print("Ja! Helaas vervaagt de kleur wel snel")

if antwoord1 == "c" or antwoord1 == "C":
    print("Nope, maar wel in de buurt")

if antwoord1 == "d" or antwoord1 == "D":
    print("Nee, dit is mijn echte haarkleur...")

else:
    print("ik begrijp alleen maar a, b, c ofd als antwoord")

 
