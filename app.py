import random

def skaiciai():
    global skaicius1_sudetis
    skaicius1_sudetis = random.randint(1, 100)
    global skaicius2_sudetis
    skaicius2_sudetis = random.randint(1, 100)
    global skaicius1_atimtis
    skaicius1_atimtis = random.randint(1, 100)
    global skaicius2_atimtis
    skaicius2_atimtis = random.randint(1, 100)
    global skaicius1_daugyba
    skaicius1_daugyba = random.randint(1, 20)
    global skaicius2_daugyba
    skaicius2_daugyba = random.randint(1, 20)


def pasirinkimas():
    matematika = random.choice(["sudetis", "atimtis", "daugyba"])
    if matematika == "sudetis":
        sudetis()
    elif matematika == "atimtis":
        atimtis()
    elif matematika == "daugyba":
        daugyba()

def sudetis():
    teisingas_sudetis = skaicius1_sudetis + skaicius2_sudetis
    atsakymas_sudetis = int(input(f"Kiek bus {skaicius1_sudetis} + {skaicius2_sudetis}? "))
    if atsakymas_sudetis == teisingas_sudetis:
        print("teisingai")
    else:
        print("neteisingai")

if pasirinkimas == "sudetis":
    sudetis()


def atimtis():
    teisingas_atimtis = skaicius1_atimtis - skaicius2_atimtis
    atsakymas_atimtis = int(input(f"Kiek bus {skaicius1_atimtis} - {skaicius2_atimtis}? "))
    if atsakymas_atimtis == teisingas_atimtis:
        print("teisingai")
    else:
        print("neteisingai")

if pasirinkimas == "atimtis":
    atimtis()


def daugyba():
    teisingas_daugyba = skaicius1_daugyba * skaicius2_daugyba
    atsakymas_daugyba = int(input(f"Kiek bus {skaicius1_daugyba} * {skaicius2_daugyba}? "))
    if atsakymas_daugyba == teisingas_daugyba:
        print("teisingai")
    else:
        print("neteisingai")

if pasirinkimas == "daugyba":
    daugyba()

while True:
    skaiciai()
    pasirinkimas()
    if input("Zaisti toliau? (taip/ne): ") != "taip":
        break


