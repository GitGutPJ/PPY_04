mojaLista = []
for i in range (0,3):
    liczba = input("Podaj liczbe roznaprzecinkowa")
    liczba = float(liczba)
    mojaLista.insert(i,liczba)
print(mojaLista,'\n')
maximum = mojaLista[0]
minimum = mojaLista[0]
for index in mojaLista:
    if(maximum<index):
        maximum = index
    if(minimum>index):
        minimum = index
print('Maksimum: ',maximum,'\n')
print('Minimum: ',minimum)