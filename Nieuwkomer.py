import os
import time

def restart():
    restart = input("Wil je dit avontuur nog een keer doen? Type Y/N: ").upper()
    if restart == "Y":
        main()
    elif restart == "N":
        print("Oke")
    
    else:
        print("Verkeerde invoer, alleen Y of N")
        main()

def einde1():
    print("doodlopend einde")
def einde2():
    print("normaal einde")
def einde3():
    print("slecht einde")
def einde4():
    print("goed einde")
    

#hier moet een kort intro stukje komen.
def intro():
    print("In dit verhaal ben je een man die in Afghanistan woont. Je woont hier met je gezin van 5. Je bent best gelukkig en hebt een goede baan. Op een dood normale dag word je opgebeld door een goede vriend die 2 steden verderop woont. Hij vertelt je dat het echt niet meer veilig is om hier te blijven en dat je moet vluchten. Hij kan regelen dat je met een busje het land uit kan, maar dat kost je wel geld. €2000,- wel geteld. Dit geld heb je op je spaar rekening staan, maar wil dat liever achterlaten voor je familie.")
    print("1. Wat ga je doen?")
    print("A: Je wacht tot je het geld hebt kunnen verzamelen. Je werkt extra en verkoopt een stuk land wat je nog in je bezit had.")
    print("B: Je kiest er voor om die €2000,- van je spaar rekening te halen, je vrouw werkt tevens ook dus dat moet wel goed komen. ")
    intro = input("A of B? ").upper()
    if intro == "A":
        print("----------------------------------------------------------------------------------")
        stukje14()
    elif intro == "B":
        print("----------------------------------------------------------------------------------")
        stukje131()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        intro()

time.sleep(1)
#stukje 1
def stukje1():
    print("1. intro txt?")
    print("A: txt4")
    print("B: txt4")
    stukje1 = input("A of B? ").upper()
    if stukje1 == "A":
        print("----------------------------------------------------------------------------------")
        stukje4()
    elif stukje1 == "B":
        print("----------------------------------------------------------------------------------")
        stukje4()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje1()

#stukje 2
def stukje2():
    print("2. intro txt?")
    print("A: txt18")
    print("B: txt21")
    print("C: txt1")
    stukje2 = input("A, B of C? ").upper()
    if stukje2 == "A":
        print("----------------------------------------------------------------------------------")
        stukje18()
    elif stukje2 == "B":
        print("----------------------------------------------------------------------------------")
        stukje21()
    elif stukje2 == "B":
        print("----------------------------------------------------------------------------------")
        stukje1()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje2()

#stukje 3
def stukje3():
    print("3. intro txt?")
    print("A: txt18")
    print("B: txt21")
    stukje3 = input("A of B? ").upper()
    if stukje3 == "A":
        print("----------------------------------------------------------------------------------")
        stukje11()
    elif stukje3 == "B":
        print("----------------------------------------------------------------------------------")
        stukje17()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje3()

#stukje 4
def stukje4():
    print("4. intro txt?")
    print("A: txt10")
    print("B: txt18")
    stukje4 = input("A of B? ").upper()
    if stukje4 == "A":
        print("----------------------------------------------------------------------------------")
        stukje10()
    elif stukje4 == "B":
        print("----------------------------------------------------------------------------------")
        stukje18()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje4()

#stukje 5 = einde1
def stukje5():
    einde1()
    restart()

#stukje 6
def stukje6():
    print("6. intro txt?")
    print("A: txt4")
    print("B: txt4")
    stukje6 = input("A of B? ").upper()
    if stukje6 == "A":
        print("----------------------------------------------------------------------------------")
        stukje4()
    elif stukje6 == "B":
        print("----------------------------------------------------------------------------------")
        stukje4()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje6()

#stukje 7 = einde2
def stukje7():
    einde2()
    restart()

#stukje 8 gaat naar stukje 10
def stukje8():
    stukje10()

#stukje 9
def stukje9():
    print("9. intro txt?")
    print("A: txt20")
    print("B: txt16")
    stukje9 = input("A of B? ").upper()
    if stukje9 == "A":
        print("----------------------------------------------------------------------------------")
        stukje20()
    elif stukje9 == "B":
        print("----------------------------------------------------------------------------------")
        stukje16()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje9()

#stukje 10
def stukje10():
    print("10. intro txt?")
    print("A: txt9")
    print("B: txt15")
    stukje10 = input("A of B? ").upper()
    if stukje10 == "A":
        print("----------------------------------------------------------------------------------")
        stukje9()
    elif stukje10 == "B":
        print("----------------------------------------------------------------------------------")
        stukje15()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje10()
        
#stukje 11 = einde1
def stukje11():
    einde1()
    restart()
    
#stukje 12
def stukje12():
    print("12. intro txt?")
    print("A: txt6")
    print("B: txt3")
    stukje12 = input("A of B? ").upper()
    if stukje12 == "A":
        print("----------------------------------------------------------------------------------")
        stukje6()
    elif stukje12 == "B":
        print("----------------------------------------------------------------------------------")
        stukje3()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje12()

#stukje 13.1
def stukje131():
    print("13. Nadat je het geld hebt geregeld bel je je vriend die de bus ook zou regelen. Hij heeft ook en nieuw paspoort voor je geregeld, zodat je iets hebt als je het land verlaat. Morgen ochtend word je om 9:00 uur verwacht bij de moskee aan de rand van het dorp. Je twijfelt of je een tas met wat noodzakelijke spullen te pakken voor je lange reis. Wat doe je?")
    print("A: Je pakt een kleine rugzak in met wat noodzakelijke spullen.")
    print("B: Je neemt geen tas mee, omdat je vast niet de enige zal zijn in dat busje. Het belangrijkste stop je wel in je zakken.")
    stukje131 = input("A of B? ").upper()
    if stukje131 == "A":
        print("----------------------------------------------------------------------------------")
        stukje5()
    elif stukje131 == "B":
        print("----------------------------------------------------------------------------------")
        stukje3()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje131()

#stukje 13.2
def stukje132():
    print("13. Je hebt besloten om toch wel met het busje te gaan. Morgen ochtend word je om 9:00 uur verwacht bij de moskee aan de rand van het dorp. Je twijfelt of je een tas met wat noodzakelijke spullen te pakken voor je lange reis. Wat doe je?")
    print("A: Je pakt een kleine rugzak in met wat noodzakelijke spullen.")
    print("B: Je neemt geen tas mee, omdat je vast niet de enige zal zijn in dat busje. Het belangrijkste stop je wel in je zakken.")
    stukje132 = input("A of B? ").upper()
    if stukje132 == "A":
        print("----------------------------------------------------------------------------------")
        stukje5()
    elif stukje132 == "B":
        print("----------------------------------------------------------------------------------")
        stukje3()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje132()

#stukje 14
def stukje14():
    print("14. Het is je gelukt om het geld zo snel mogelijk te verzamelen en je belt de vriend op die het busje voor je kon regelen. Die vriend zou ook een nieuw paspoort regelen, zodat je in ieder geval iets hebt. Je gaat bij die vriend langs om je nieuwe paspoort op te halen. Eenmaal terug thuis twijfel je of je wel met het busje mee gaat. Wat ga je doen?")
    print("A: Je gaat wel met het busje mee en je hoopt op het beste.")
    print("B: Je besluit niet mee te gaan met het busje en besluit te gaan lopen.")
    stukje14 = input("A of B? ").upper()
    if stukje14 == "A":
        print("----------------------------------------------------------------------------------")
        stukje132()
    elif stukje14 == "B":
        print("----------------------------------------------------------------------------------")
        stukje2()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje14()

#stukje 15 = einde1
def stukje15():
    einde1()
    restart()

#stukje 16 = einde3
def stukje16():
    einde3()
    restart()

#stukje 17 = einde1
def stukje17():
    einde1()
    restart()

#stukje 18
def stukje18():
    print("18. intro txt?")
    print("A: txt13")
    print("B: txt2")
    stukje18 = input("A of B? ").upper()
    if stukje18 == "A":
        print("----------------------------------------------------------------------------------")
        stukje10()
    elif stukje18 == "B":
        print("----------------------------------------------------------------------------------")
        stukje8()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje18()

#stukje 19
def stukje19():
    print("19. intro txt?")
    print("A: txt12")
    print("B: txt7")
    stukje19 = input("A of B? ").upper()
    if stukje19 == "A":
        print("----------------------------------------------------------------------------------")
        stukje12()
    elif stukje19 == "B":
        print("----------------------------------------------------------------------------------")
        stukje7()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje19()

#stukje 20 = einde4
def stukje20():
    einde4()
    restart()

#stukje 21 = einde1
def stukje21():
    einde1()
    restart()


def main():
    print("Hey! Welkom bij dit avontuur gebasseerd op het verhaal van een vluchteling")
    print("Voordat we beginnen heb ik nog een vraag voor je")
    naam = input("Wat is jouw naam? ")
    print("Top. Laten we beginnen " + naam + "!")
    intro()
    stukje1()
    restart()
    
main()
