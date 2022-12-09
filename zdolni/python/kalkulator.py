def dod(a,b):
    c = a+b
    print(c)
    			
def odejm(a,b):
	c = a-b
	print(c)

def mnoz(a,b):
	c=a*b
	print(c)
	
def dziel(a,b):
	c = a/b
	print(c)
# def poteg(a,b):
# 	c = a**b
#     print(c)
def poteg(a,b):
    c = a**b
    print(c)
	
def silnia(a):
    if a == 1:
        fact = 1
        print(fact)
    else:
        for i in range(1, a+1):
            fact = fact * i
        print(fact)

    
        
def bin(a):
    if a >= 1:
        bin(a // 2)
        print(a % 2)
    else: 
        print(1)

def oct(a):
    octal = 0
    ctr = 0
    while(a>0):
        octal += ((a%8)*(10**ctr))  
        ctr+=1

    print(octal)

    # ctr = 0
	# while(a > 0):
    # 	octal += ((a%8)*(10**ctr))  
    #     a = int(a/8)            
    #     ctr += 1
   	 
def decimalToHexadecimal(decimal):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    print(hexadecimal)
        
        
while(True):
    print("proszę wybrać: ")
    print("1) Dodawanie")
    print("2) Odejmowanie")
    print("3) Monżenie")
    print("4) Dzielenie")
    print("5) Potęgowanie")
    print("6) Silnia")
    print("7) System binarny (dwójkowy)")
    print("8) System oktalny (ósemkowy)")
    print("9) System heksadecymalny (szesnastkowy)")
    print("10) Wyjście z programu")                                                    
    odp = int(input())
    try:
        int(odp)
        jest = True
    except ValueError:
        jest = False
       
    if odp < 1 or odp > 10 or jest == False:
        while( True):
            print("Proszę wprowadzić prawidłową liczbę")
            odp = int(input())
            if odp <10 and odp >= 1 and jest == True:
                if odp == 1: 
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    dod(p,d)
                    break
                elif odp == 2:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
                elif odp == 3:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    mnoz(p,d)
                    break
                elif odp == 4:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
                elif odp == 5:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
                elif odp == 6:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
                elif odp == 7:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
                elif odp == 8:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
                elif odp == 9:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
                elif odp == 10:
                    p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
                    d = float(input())
                    odejm(p,d)
                    break
    else:
        if odp == 1: 
            p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
            d = float(input())
            dod(p,d)
            break
