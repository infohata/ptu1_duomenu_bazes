class Puodelis:
    talpa_ml = 50
    pavadinimas = "Espresso"
    pilnas = False


def ipilti_kavos():
    espresso_puodelis.pilnas = True
    print("ipilam kavos...")
    isorinis_kintamasis = False
    print(f"bandom skleist {isorinis_kintamasis} propaganda...")



espresso_puodelis = Puodelis()
isorinis_kintamasis = True

print(f"ar pilnas puodelis: {espresso_puodelis.pilnas}, ir tikra tiesa: {isorinis_kintamasis}")
ipilti_kavos()
print(f"ar pilnas puodelis: {espresso_puodelis.pilnas}, ir tikra tiesa: {isorinis_kintamasis}")
