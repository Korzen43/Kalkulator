while True:
    operacja = input("Podaj dzialanie ktore chcesz wykonac : \n1.Dodawanie \n2.Odejmowanie \n3.Mnozenie \n4.Dzielenie \n5.Potegowanie \n6.Pierwiatek \n")
    def zapytaj_o_dwie_liczby():
        liczba1 = float(input("Podaj pierwsza liczbe "))
        liczba2 = float(input("Podaj druga liczbe: "))
        return liczba1, liczba2
    def zapyta_o_pierwsza_pierwsza():
        a = float(input("Podaj pierwsza liczbe "))
        return a
    if (operacja == "1"):
        a ,b = zapytaj_o_dwie_liczby()
        print(a+b)
        
        
       
    elif (operacja =="2"):
        
        
        print(a-b)
    elif (operacja =="3"):
       
        
        print(a*b)
    elif (operacja =="4"):
        try:
            
            print(a/b)
        except ZeroDivisionError as Error:
            print("Bledna opreacja , nie dzielimy przez ZERO")
            
    elif (operacja =="5"):
        
        print(a**b)
    elif (operacja =="6"):
        
        print(a ** 0.5)
    ponowna_oporecacja = input("Czy chcesz wykonac ponowna operacje Tak lub Nie  \n")
    if ponowna_oporecacja == ("Nie") :
        break




