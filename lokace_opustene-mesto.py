import random
import sys



prozkoumal_obchod = False
prozkoumal_hluk = False
body = 0
dalsi_level = False

def konec_hry():
    sys.exit()

def opustene_mesto():
    global prozkoumal_obchod, prozkoumal_hluk, body, dalsi_level
    while True:
        print("\nDorazil jsi do opuštěného města. Všude kolem jsou trosky a ticho tě tíží.")
        

        if prozkoumal_obchod and prozkoumal_hluk:
            volba = input("Co uděláš dál? (2 = Schovat se a počkat): ")
        elif prozkoumal_obchod:
            volba = input("Co uděláš dál? (2 = Schovat se a počkat, 3 = Jít za hlukem): ")
        elif prozkoumal_hluk:
            volba = input("Co uděláš dál? (1 = Prozkoumat obchod, 2 = Schovat se a počkat): ")
        else:
            volba = input("Vidíš otevřený obchod a slyšíš vzdálený hluk. Co uděláš? (1 = Prozkoumat obchod, 2 = Schovat se a počkat, 3 = Jít za hlukem): ")



        if volba == "1" and not prozkoumal_obchod:
            if random.randint(1, 2) == 1:
                print("Našel jsi zásoby jídla a vody! Získáváš 2 body za přežití.")
                body += 2
                prozkoumal_obchod = True
                print(f"Máš {body} bodů a vracíš se zpátky")
                
            else:
                print("Našel jsi prázdné plechovky a rozbité lahve. Získáváš 1 bod za odpad, který můžeš recyklovat.")
                body += 1
                prozkoumal_obchod = True
                print(f"Máš {body} bodů a vracíš se zpátky")



        elif volba == "2":
            if random.randint(1, 4) == 1:
                print("Počkání se vyplatilo, hluk utichl. Získáváš 6 bodů za obezřetnost.")
                return
            else:
                print("Hlídka tě zahlédla a začíná tě pronásledovat!")
                print("\nMusíš se rychle rozhodnout, kam utéct!")
                volba_uteku = input("Kam se schováš? (1 = Ulička, 2 = Popelnice, 3 = Vylézt po žebříku): ")
                if volba_uteku == "1" or volba_uteku == "3":
                    print("Podařilo se ti utéct! Hlídka tě ztratila z dohledu.")
                    body += 3
                    dalsi_level = True
                    return
                elif volba_uteku == "2":
                    print("Schoval ses do popelnice, ale hlídka tě našla. Hra končí.")
                    konec_hry
                    return
                else:
                    print("Neplatná volba, hlídka tě dostala. Hra končí.")
                    return



        elif volba == "3" and not prozkoumal_hluk:
            if random.randint(1, 3) == 1:
                print("Našel jsi přeživšího, který ti pomůže! Získáváš 3 body za spojenectví.")
                body += 3
                prozkoumal_hluk = True
                print(f"Máš {body} bodů a vracíš se zpátky")

            elif random.randint(1, 3) == 2:
                print("Bylo to stádo divokých zvířat, musíš utéct. Ztrácíš 1 bod.")
                body += -1
                prozkoumal_hluk = True
                print(f"Máš {body} bodů a vracíš se zpátky")

            else:
                print("Byl to zvuk zřícení budovy, ale našel jsi něco užitečného. Získáváš 1 bod.")
                body += 1
                prozkoumal_hluk = True
                print(f"Máš {body} bodů a vracíš se zpátky")

        else:
            print("Neplatná volba. Zkus to znovu.")

opustene_mesto()
