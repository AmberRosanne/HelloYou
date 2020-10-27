import time

a = True
while a == True:
    hello = "Hello You! Ik ben {owner}. Wie ben jij?"
    print(hello.format(owner = "Amber"))

    time.sleep (1)

    username = input("Mijn naam is:")
    print("Hoi " + username, "! Dit is de datum:")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("Vandaag is het " + x.strftime("%d"), " " + x.strftime ("%B"))
    while True: 
             query = input('Wil je doorgaan? Y/N')
             Fl = query[0].lower()
             if query == '' or not Fl in ['y','n']: 
                print('Kies Yes of No als antwoord!') 
             else: 
                break 
    if Fl == 'y': 
            print("Yeayy! Nog een keer! :)")
    if Fl == 'n': 
             break 