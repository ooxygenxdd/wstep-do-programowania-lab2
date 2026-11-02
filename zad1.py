punkty = int(input("Podaj liczbę punktów: "))

if punkty > 80:
    print("Zaliczyłeś egzamin w terminie 0")
elif punkty >= 50:
    print("Możesz poprawić wynik")
else:
    print("Musisz poprawić egzamin")
