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
    fact = 1
    if a == 1:
        fact = 1
        print(fact)
    else:
        for i in range(1, a+1):
            fact = fact * i
        print(fact)

    
        
def binn(n):
    a =  bin(n).replace("0b", "")
    print(a)

def octt(a):
    octal = oct(a).replace("0o", "")
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
        
def dwie():  
    try:
        p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
        try:
            d = float(input())
            return p,d
            
        except ValueError:
            while True:
                try:
                    d = float(input("Proszę wprowadzić prawidłową liczbę: "))
                    return p,d
                    
                except ValueError:
                    continue    
    except ValueError:
        
        while True:
            try:
                p = float(input("Proszę wprowadzić prawidłową liczbę: "))
                while True:
                    try:
                        d = float(input()) 
                        return p,d
                    except ValueError:
                        print("Proszę wprowadzić prawidłową liczbę: ")
            except ValueError:
                continue     

def jedna():  
    try:
        p = int(input("Wpisz liczbe calkowita: "))
        return p   
    except ValueError:
        
        while True:
            try:
                p = int(input("Proszę wprowadzić prawidłową liczbę: "))
                return p
            except ValueError:
                continue 
            
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
    
       
    # if odp < 1 or odp > 10 or jest == False:
    
    #         odp = int(input())
    #         if odp <10 and odp >= 1 and jest == True:
    if odp == 1:    
        p,d = dwie()
        dod(p,d)
    elif odp == 2:
        p,d = dwie()
        odejm(p,d)
        
    elif odp == 3:
        p,d = dwie()
        mnoz(p,d)
        
    elif odp == 4:
        p,d = dwie()
        dziel(p,d)
        
    elif odp == 5:
        p = jedna()
        b = jedna()
        poteg(p,b)
        
    elif odp == 6:
        p = jedna()
        silnia(p)
        
    elif odp == 7:
        p = jedna()
        binn(p)
        
    elif odp == 8:
        p = jedna()
        octt(p)
        
    elif odp == 9:
        p = jedna()
        decimalToHexadecimal(p)
        
    elif odp == 10:
        break
        
    # else:
    #     if odp == 1: 
    #         p = float(input("Wpisz dwie cyfry rzeczywiste (po kolei): "))
    #         d = float(input())
    #         dod(p,d)
    #         break
