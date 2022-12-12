def strike():
    pkt1 = int(input("liczba punktow zdobyta po strike'u (rzut 1): "))
    pkt2 = int(input("liczba punktow zdobyta po strike'u (rzut 2): "))
    c = pkt1 + pkt2
    return c
def spare():
    pkt1 = int(input("liczba punktow zdobyta po spare: "))
    return pkt1

def miss():
    print('Miss')


runda = {}
gracze = []

l_graczy = int(input("Podaj liczbe graczy: "))

for k in range(0, l_graczy):
    for l in range(10):
        
        gracze[k].append(' ')
    # gracze[k].append(f'Gracz nr. {k+1}')



# for i in range(10):
i = 0
while(i>10):
    print(f"Runda {i+1}")
    for j in range(0, len(l_graczy)):
        points = 0
        for r in range(2):
            print(f"Gracz nr.{j+1} - rzut nr.{r+1}")
            krgl = int(input("Zbite kręgle: "))
            points += krgl
            if points == 10 and r == 1:
                #krgl = 10
                o = strike()
                points += o
                break
            elif points == 10 and r == 2:
                #krgl = 10
                o = spare()
                points+=o
            elif points == 0 and r == 2:
                miss()    
            elif points < 10:
                continue
        
        gracze[j][i] = points
    ### dac do tablicy 
    tab = []
    ### tab[0] = 1,2, ..., 9,10
    ### tab[1] = gracz 1 ... points
    for g in range(len(gracze)+1):
        if g == 0:
            tab[g] = ['             1   2   3   4   5   6   7   8   9   10']
        else:
            for h in range(0,10):
                tab[g].append(f'Gracz nr. {g}')
                if len(str(gracze[g-1][h])) == 3:
                    # tab.append(f'Gracz nr. {g} ')
                    tab[g].append(f' {gracze[g-1][h]}')
                elif len(str(gracze[g-1][h])) == 2:
                    # tab.append(f'Gracz nr. {g} ')
                    tab[g].append(f'  {gracze[g-1][h]}')
                elif len(str(gracze[g-1][h])) == 1 and gracze[g-1][h] != ' ':
                    # tab.append(f'Gracz nr. {g} ')
                    tab[g].append(f'  {gracze[g-1][h]} ')
                elif len(str(gracze[g-1][h])) == 1 and gracze[g-1][h] == ' ':
                    # tab.append(f'Gracz nr. {g} ')
                    continue

    for d in range(len(tab)):
        print(*tab[d])

    i+=1


            

