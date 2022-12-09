import random
lol = 0
oceny = []
wagi = []
przedmioty = ["Polskiego", "Matematyki", "Angielskiego", "Informatyki", "Fizyki", "Biologii", "Francuskiego"]
dlr = random.randint(0, len(przedmioty))
while True:
    lo = int(input("Prosze podać liczbę ocen: "))
    

    if lo<=30:
    	break
    elif lo>30 and lol == 0:
    	print("Za duża liczba ocen")
    	lol = 5
    if(lol!=0):
    	print("Proszę wprowadzić liczbę całkowitą w zakresie od 1 do 30\n")	
while(lo>0): 
    dlr = random.randint(0, len(przedmioty))
    ocenka =int( input(f'Proszę podać ocene z {przedmioty[dlr]}'))
    if(ocenka>6 or ocenka <1):
    	while(True): 
    	    print("Nieprawidłowa ocena, proszę wprowadzić ponownie")
            ocenka =int( input())
            if(ocenka >0 and ocenka <=6):
                oceny.append(ocenka)
                wazka = int(input(f"podaj wage oceny z {przedmioty[dlr]}: "))
                if(wazka <1 or wazka>5):
                    while(True):
                        wazka = int(input("Proszę wprowadzić liczbę całkowitą w zakresie od 1 do 5: "))
                        if(wazka >0 and wazka < 6):
                            break