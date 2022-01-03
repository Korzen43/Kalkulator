operacja = input("Podaj dzialanie ktore chcesz wykonac : \n1.Dodawanie \n2.Odejmowanie \n3.Mnozenie \n4.Dzielenie \n5.Potegowanie \n6.Pierwiatek \n")

if (operacja == "1"):
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: ")) 
    print(a+b)
elif (operacja =="2"):
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    print(a-b)
elif (operacja =="3"):
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    print(a*b)
elif (operacja =="4"):
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    print(a/b)
elif (operacja =="5"):
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    print(a**b)
elif (operacja =="6"):
    a = float(input("Podaj pierwsza liczbe: "))
    print(a ** 0.5)

