import random

def srednia(oceny, wagi):
    licznik = 0
    mianownik = 0
    for i in range(len(oceny) ):
        print(f"")
        licznik += oceny[i] * wagi[i]
        mianownik += wagi[i]
    sra =  "{0:.2f}".format(licznik/mianownik)
    print(sra)
    
    #if sra > 4.75:
    #     print
    # print(sra)


lol = 0
oceny = []
wagi = []
przedmioty2 = []
przedmioty = ["Polskiego", "Matematyki", "Angielskiego", "Informatyki", "Fizyki", "Biologii", "Francuskiego"]
dlr = random.randint(0, len(przedmioty))
while True:
    lo = int(input("Prosze podać liczbę ocen: "))

    if lo <= 30:
        break
    if lo>30 and lol == 0:
        print("Za duża liczba ocen")
        lol = 5
    elif lol != 0 and lol != 0:
    	print("Proszę wprowadzić liczbę całkowitą w zakresie od 1 do 30")	

while lo > 0: 
    dlr = random.randint(0, len(przedmioty)-1)
    ocenka = float(input(f'Proszę podać ocene z {przedmioty[dlr]}: '))

    if ocenka > 6 or ocenka < 1:
        whbr = 1
        while whbr == 1:
            print('Nieprawidłowa ocena, proszę wprowadzić ponownie:')
            ocenka = float(input())
            if ocenka > 0 and ocenka <= 6:
                oceny.append(ocenka)

                wazka = float(input(f'Proszę podać wagę oceny z {przedmioty[dlr]}: '))
                if wazka < 1 or wazka > 5:
                    while True:
                        wazka = float(input('Proszę wprowadzić liczbę całkowitą w zakresie od 1 do 5: '))
                        if wazka > 0 and wazka < 6:
                            wagi.append(wazka)
                            whbr = 0
                            lo -= 1
                            break
                else: 
                    wagi.append(wazka)
                    whbr = 0
                    lo -= 1
                    break
    else:
        oceny.append(ocenka)

        wazka = float(input(f'Proszę podać wagę oceny z {przedmioty[dlr]}: '))
        if wazka < 1 or wazka > 5:
            while True:
                wazka = float(input('Proszę wprowadzić liczbę całkowitą w zakresie od 1 do 5: '))
                if wazka > 0 and wazka < 6:
                    wagi.append(wazka)
                    whbr = 0
                    lo -= 1
                    break
        else:
            wagi.append(wazka)
            whbr = 0
            lo -= 1
                  

srednia(oceny, wagi)           
            
            
### KLAWISZ ESC + WYPISANIE PRZEDMIOTÓW + 4.75