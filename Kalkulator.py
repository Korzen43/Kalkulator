while True:
    operacja = input("Podaj dzialanie ktore chcesz wykonac : \n1.Dodawanie \n2.Odejmowanie \n3.Mnozenie \n4.Dzielenie \n5.Potegowanie \n6.Pierwiatek \n")
    a = float(input("Podaj pierwsza liczbe: "))
    if (operacja == "1"):
        
        b = float(input("Podaj druga liczbe: ")) 
        print(a+b)
    elif (operacja =="2"):
        
        b = float(input("Podaj druga liczbe: "))
        print(a-b)
    elif (operacja =="3"):
       
        b = float(input("Podaj druga liczbe: "))
        print(a*b)
    elif (operacja =="4"):
        try:
            
            b = float(input("Podaj druga liczbe: "))
            print(a/b)
        except ZeroDivisionError as Error:
            print("Bledna opreacja , nie dzielimy przez ZERO")
            
    elif (operacja =="5"):
        
        b = float(input("Podaj druga liczbe: "))
        print(a**b)
    elif (operacja =="6"):
        
        print(a ** 0.5)
    ponowna_oporecacja = input("Czy chcesz wykonac ponowna operacje Tak lub Nie  \n")
    if ponowna_oporecacja == ("Nie") :
        break




