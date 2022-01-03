operacja = input("Podaj dzialanie ktore chcesz wykonac : \n1.Dodawanie \n2.Odejmowanie \n3.Mnozenie \n4.Dzielenie \n5.Potegowanie \n6.Pierwiatek")



if (operacja == "1"):
    print(a+b)
elif (operacja =="2"):
    print(a-b)
elif (operacja =="3"):
    print(a*b)
elif (operacja =="4"):
    print(a/b)
elif (operacja =="5"):
    print(a**b)
elif (operacja =="6"):
    print(a ** 0.5)

a = float(input("Podaj pierwsza liczbe: "))
b = float(input("Podaj druga liczbe: "))
