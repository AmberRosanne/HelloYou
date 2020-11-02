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
    print("EINDE1:")
    print("Helaas is het je niet gelukt om te vluchten. Je avontuur eindigt hier...")
def einde2():
    print("EINDE2:")
    print("Je hebt een normaal einde! Het is je gelukt om te vluchten, maar je bent niet op je bestemming die je wilde. Je hebt het nu veel beter dan in je thuis land Afghanistan.")
def einde3():
    print("EINDE3")
    print("Helaas ga je hier nog jaren zitten. Je avontuur eindigt hier...")
def einde4():
    print("EINDE4")
    print("Je bent blij en opgelucht dat het goed afgelopen is. Je avontuur eindigt hier...")
def einde5():
    print("EINDE5")
    print("Helaas ben je overleden. Je avontuur eindigt hier...")
    
#hier moet een kort intro stukje komen.
def intro():
    print("In dit verhaal ben je een man die in Afghanistan woont. Je woont hier met je gezin van 5. Je bent best gelukkig en hebt een goede baan. Op een dood normale dag word je opgebeld door een goede vriend die 2 steden verderop woont. Hij vertelt je dat het echt niet meer veilig is om hier te blijven en dat je moet vluchten. Hij kan regelen dat je met een busje het land uit kan, maar dat kost je wel geld. €2000,- wel geteld. Dit geld heb je op je spaar rekening staan, maar wil dat liever achterlaten voor je familie.")
    print("1. Wat ga je doen?")
    print("A: Je wacht tot je het geld hebt kunnen verzamelen. Je werkt extra en verkoopt een stuk land wat je nog in je bezit had.")
    print("B: Je kiest er voor om die €2000,- van je spaar rekening te halen, je vrouw werkt tevens ook dus dat moet wel goed komen.")
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


#stukje 1
def stukje1():
    print("1. Nu je toch hebt besloten met het busje te gaan heb je een lange reis te gaan. Je bent heel lang onderweg (aantal weken) en je stopt weinig. Het is een zware reis. Zodra je de grens overgaat en nog maar een paar uur moet rijden tot je in Servië aankomt vraagt een reisgenoot of je een simpel spelletje wilt doen zodat de tijd wat sneller gaat. Wat doe je?")
    print("A: Je zegt ja, je kan wel wat vermaak gebruiken. Je hebt heel veel lol en de tijd gaat een stuk sneller. ")
    print("B: Je zegt nee, je bent heel moe en wilt proberen te slapen. Je hebt tevens nog genoeg energie nodig. ")
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
        
time.sleep(1)
#stukje 2
def stukje2():
    print("2. Oké. Je gaat niet mee met het busje, maar wat ga je wel doen?")
    print("A: Je vraagt aan een vriend of hij je naar de grens bij Iran kan brengen. Zou een ander busje staan waar je je reis mee kan vervolgen.")
    print("B: Je besluit alles te gaan lopen en kijkt wel hoe ver je komt. Je wilt in ieder geval weg uit dit land.")
    print("C: Je besluit alsnog om met het busje mee te gaan.")
    stukje2 = input("A, B of C? ").upper()
    if stukje2 == "A":
        print("----------------------------------------------------------------------------------")
        stukje18()
    elif stukje2 == "B":
        print("----------------------------------------------------------------------------------")
        stukje21()
    elif stukje2 == "C":
        print("----------------------------------------------------------------------------------")
        stukje1()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a, b of c als antwoord.")
        stukje2()

time.sleep(1)
#stukje 3
def stukje3():
    print("3. Je bent verder gaan lopen en na een aantal dagen lopen ben je helemaal gesloopt, je hoopt dat je nog iets van eten en drinken kan bietsen bij mensen op straat. Je bent behoorlijk moe en hebt pijnlijke voeten. Wat ga je doen?")
    print("A: Je hebt zo’n honger en bent zo moe dat je een plekje zoekt om even te kunnen zitten. Al snel zie je een bankje in een park waar je op gaat liggen. ")
    print("B: Je zoekt naar wat oude dozen bij het afval en gaat daar op liggen en je slaapt op straat. Je hebt nou eenmaal echt even slaap nodig.")
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

time.sleep(1)
#stukje 4
def stukje4():
    print("4. Na nog wat uren moet je net na de grens van Kroatië opeens stoppen. Er is pech. Het busje moet naar de plaatselijke garage om gerepareerd te worden. Hoe lang gaat dit duren?")
    print("A: Niet lang, het is een klein probleem en na een paar uur kan je de reis vervolgen.")
    print("B: Langer dan verwacht en je loopt “vertraging” op.")
    stukje4 = input("A of B? ").upper()
    if stukje4 == "A":
        print("----------------------------------------------------------------------------------")
        stukje10()
    elif stukje4 == "B":
        print("----------------------------------------------------------------------------------")
        stukje81()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje4()

time.sleep(1)
#stukje 5 = einde1
def stukje5():
    print("Je komt in de ochtend aan bij de afgesproken plek waar het busje al op je staat te wachten. Op het moment dat je er heen loopt om in te stappen spreekt de man je aan over je tas. Je mag je tas niet mee nemen, aangezien hij nog 10 mensen moet mee nemen. Je kans om te vluchten vervalt en je gaat weer teleurgesteld naar huis.")
    einde1()
    restart()

time.sleep(1)
#stukje 6
def stukje6():
    print("6. Na een week wachten is het busje eindelijk gerepareerd en kan je je reis vervolgen. Na dat je ongeveer over de helft bent vraagt je reisgenoot of je een simpel spelletje wilt doen zodat de tijd wat sneller gaat. Wat doe je?")
    print("A: Je zegt ja, je kan wel wat vermaak gebruiken. Je hebt heel veel lol en de tijd gaat een stuk sneller.")
    print("B: Je zegt nee, je bent heel moe en wilt proberen te slapen. Je hebt tevens nog genoeg energie nodig.")
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

time.sleep(1)
#stukje 7 = einde2
def stukje7():
    print("Na 3 dagen te wachten is het busje gerepareerd. Je hebt afgesproken dat je om 20:00 in de avond weer bij de garage te zijn. Doordat je zelf op verkenning bent gegaan vergeet je de tijd die je hebt afgesproken en besef je je veel te laat dat het al 20:00 is geweest. Je bent “gestrand” in Griekenland en gaat richting het asielzoekers centrum. Dit alles verloopt goed en een jaar later heb je een goede woning en nieuw werk.")
    einde2()
    restart()

time.sleep(1)
#stukje 8 gaat naar stukje 10
def stukje81():
    print("Eenmaal aangekomen wacht je bij de garage.")
    stukje10()

time.sleep(1)
#stukje 8 gaat naar stukje 10
def stukje82():
    print("Na 2 dagen is de bus eindelijk gerepareerd.")
    stukje10()

time.sleep(1)
#stukje 9
def stukje9():
    print("9. Je rijdt aan lange stukken door en komt eindelijk in Oostenrijk aan. Zodra je bij de grens naar Duitsland wilt gaan sta je opeens stil. Er is grenscontrole en je hoopt dat je er niet uit wordt gepikt. Wat gebeurt er?")
    print("A: Na een tijdje rij je weer verder. Je bent opgelucht en blij dat je niet er uit bent gepikt. Je reis vervolgt.")
    print("B: Na een tijdje rij je een klein stukje verder en stop je weer. Je vreest voor het ergste en de achter deuren gaan open. Je bent de sjaak...")
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

time.sleep(1)
#stukje 10
def stukje10():
    print("10. Je kan eindelijk weer verder! Je reis duurt nog wel lang maar na een aantal dagen kom je aan in Kroatië. Je hoopt dat je even tijd krijgt om eten te bietsen bij wat mensen en even rond te lopen. Krijg je hier ook de tijd voor?")
    print("A: Nee, iedereen wil zo snel mogelijk verder.")
    print("B: Ja! Je bent blij en gaat op pad.")
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

time.sleep(1)    
#stukje 11 = einde1
def stukje11():
    print("Als je eenmaal op het bankje ligt voel je je steeds slechter worden en heb je overal pijn steken. Je besluit om even je ogen te sluiten en daarna je tocht te vervolgen. Je valt in slaap op het vieze, natte en harde bankje. Helaas ben je daarna ben je nooit meer wakker geworden...")
    einde5()
    restart()

time.sleep(1)  
#stukje 12
def stukje12():
    print("12. Dus je moet 2 weken wachten. Het wachten duurt je te lang en je gaat na een week bedenken wat je wilt gaan doen. Je bent op 2 opties gekomen namelijk: Optie 1, je blijft met tegenzin nog een week wachten, maar je hoopt je nog te vermaken met rondlopen en dingen bekijken. Optie2, je besluit om verder te gaan lopen en je hoopt zo ver mogelijk te komen. Voor welke optie ga je?")
    print("A: Je gaat voor optie 1. Je gaat nog 1 week wachten, ook al duurt het nog lang.")
    print("B: Je gaat voor optie 2. Je gaat verder lopen en hoopt op het beste.")
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

time.sleep(1)
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
        stukje19()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje131()

time.sleep(1)
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
        stukje19()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje132()

time.sleep(1)
#stukje 14
def stukje14():
    print("14. Het is je gelukt om het geld zo snel mogelijk te verzamelen en je belt de vriend op die het busje voor je kon regelen. Die vriend zou ook een nieuw paspoort regelen, zodat je in ieder geval iets hebt. Je gaat bij die vriend langs om je nieuwe paspoort op te halen. Eenmaal terug thuis twijfel je of je wel met het busje mee gaat. Wat ga je doen?")
    print("A: Je gaat wel met het busje mee en je hoopt op het beste.")
    print("B: Je besluit niet mee te gaan met het busje en besluit iets anders te zoeken.")
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

time.sleep(1)
#stukje 15
def stukje15():
    print("Je gaat als eerste proberen om eten te bietsen bij wat mensen en komt er al gauw achter dat de mensen hier heel aardig zijn. Nadat je je buik weer gevuld hebt en een paar flessen drinken hebt geregeld voor onderweg ga je via een mooie route weer terug naar het busje. Je vervolgt je reis.")
    stukje9()
    restart()

time.sleep(1)
#stukje 16 = einde3
def stukje16():
    print("Je bent er uit gepikt bij de grens controle en de chauffeur krijgt een flinke boete. Jij en je reisgenoten worden meegenomen naar het asiel zoekers centrum. Het is er mega druk en je bent bang dat je hier nooit uit gaat komen. Je baalt zo erg dat je bent gaan vluchten en mist je gezin zo erg...")
    einde3()
    restart()

time.sleep(1)
#stukje 17
def stukje17():
    print("Door een nacht op straat te spenderen ben je ziek geworden. Je voelt je vreselijk en kan niks meer. Door je slechte hygiëne wordt de ziekte alleen maar erger. Je besluit nog even te gaan slapen en daarna wat eten en drinken proberen te bietsen bij mensen. Je gaat weer op de dozen liggen en valt in slaap. Daarna ben je nooit meer wakker geworden...")
    einde5()
    retstart()

time.sleep(1)
#stukje 18
def stukje18():
    print("18. Eenmaal in het nieuwe busje heb je een lange reis. Na heel veel rijden, weinig stoppen en geen besef van tijd is er een lange stop. Je hebt 2 keuzes: of je stap nu over op een busje die meteen doorgaat naar Kroatië of je stapt straks in Servië over op een ander busje waar meer plek is en dus de reis iets comfortabeler wordt. Wat doe je?")
    print("A: Je stapt hier al over, je wilt dat deze reis zo snel mogelijk over is dus dan maar minder comfort.")
    print("B: Je stapt straks in Servië over op het andere busje, meer comfort klikt toch wel heel goed…")
    stukje18 = input("A of B? ").upper()
    if stukje18 == "A":
        print("----------------------------------------------------------------------------------")
        stukje10()
    elif stukje18 == "B":
        print("----------------------------------------------------------------------------------")
        stukje81()
    else:
        print("Sorry dat begrijp ik niet. Ik begrijp alleen maar a of b als antwoord.")
        stukje18()

time.sleep(1)
#stukje 19
def stukje19():
    print("19. Je komt de volgende ochtend aan bij het busje die al op je stond te wachten. Je begroet de man die bij het busje staat en stap vol zenuwen in bij het busje. Na een aantal dagen rijden bereik je Griekenland. Onderweg heb je in totaal nog 8 mensen opgehaald en zit je vrij krap achter in het busje. Net als je de grens over ben stop je opeens. Je komt er al snel achter dat je pech hebt en moet wachten. De lokale ‘wegenwacht’ wordt gebeld en ze gaan het busje repareren. Hoelang gaat het duren? ")
    print("A: Het duurt lang, er moet een onderdeel besteld worden en daardoor moet je 2 weken wachten.")
    print("B: Niet zo lang, je vervolgt je reis binnen 3 dagen.")
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

time.sleep(1)
#stukje 20 = einde4
def stukje20():
    print("Na nog zo’n 2/3 dagen rijden kom je eindelijk in Nederland aan en ga je naar het asiel zoekers centrum. Gelukkig helpen hun j e snel en heb je binnen een halfjaar een huisje en nieuw werk en mag je binnenkort de inburgering cursus starten. Je bent blij dat het vluchten gelukt is en je hebt eindelijk weer contact met je gezin.")
    einde4()
    restart()

time.sleep(1)
#stukje 21 = einde1
def stukje21():
    print("Door vermoeiing besluit je op te geven en je vriend te bellen en te vragen of hij je op haalt.")
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
