import random
def statek():
    print("\nDošel jsi na statek. Vypadá poklidně. Až moc klidně.")
    volba = input("Chtěl bys prohledat statek? (1 = Ano zkusím prohledat statek, 2 = Ne půjdu pryč): ")
    if volba == "1":
        vysledek = random.randint(1, 3)
        if vysledek == 1:
            print("Prohledal jsi důkladně celý statek a našel jsi měšec s mincemi. Získáváš 2 body.")
            return 2
        if vysledek == 2:
            print("Nechtělo se ti moc hledat a vzal jsi první věc co jsi viděl. Byl to starý zrezlý prsten. Získáváš 1 bod.")
            return 1
        else:
            print("Chtěl jsi prohledávat, ale nakonec se ti moc nechtělo. Odešel jsi.")
            return 0
    elif volba == "2":
        if random.randint(1, 20) >= 2:
            print("Díky síle odhodlání jsi odešel jsi. Přemýšlíš proč jsi sem vůbec chodil...")
            return 0
        if random.randint(1, 20) == 1:
            print("Při tom co jsi odcházel sis zlomil nohu. Nemůžeš pokračovat. Hra končí.")
            return -1
    else:
        print("Neplatná volba, vrazil jsi hlavou o roh a upadl do bezvědomí... Hra končí.")
        return -1
statek()