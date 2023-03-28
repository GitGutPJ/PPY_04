import random
import getpass

iloscRund = input('Podaj ilosc rund')
iloscRund = int(iloscRund)
komputerWybory = ["kamien","papier","nozyce"]
tryb = input('Wybierz typ:\na) komputer\nb) 2 graczy (hot seats)')
if(tryb!='a' and tryb!='b'):
    while(tryb!='a' and tryb!='b'):
        tryb = input('Wybrano niewlasciwy typ. Prosze podac ponownie: \na) komputer\nb) 2 graczy (hot seats)')
gracz1 = input('Nazwij gracza 1')
listaWynik = []
if tryb=='b':
    gracz2 = input('Nazwij gracza 2')
    for i in range (0,iloscRund):
        wybor = getpass.getpass("Wybierz:\na) kamien\nb) papier\nc) nozyce")
        wybor2 = getpass.getpass('Wybierz:\na) kamien\nb) papier\nc) nozyce')
        while(wybor!='a' and wybor!='b' and wybor!='c' and wybor2!='a' and wybor2!='b' and wybor2!='c'):
            if(wybor!='a' and wybor!='b' and wybor!='c'):
                wybor = getpass.getpass('Wybierz:\na) kamien\nb) papier\nc) nozyce')
            else:
                wybor2 = getpass.getpass('Wybierz:\na) kamien\nb) papier\nc) nozyce')
        if wybor=='a' :
            if wybor2=='a':
                listaWynik.insert(i,'Remis')
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Remis')
            elif wybor2=='b':
                listaWynik.insert(i,gracz2)
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Wygral: ',gracz2)
            else :
                listaWynik.insert(i,gracz1)
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Wygral: ',gracz1)
        elif wybor=='b' :
            if wybor2=='a':
                listaWynik.insert(i,gracz1)
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Wygral: ',gracz1)
            elif wybor2=='b':
                listaWynik.insert(i,'Remis')
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Remis')
            else :
                listaWynik.insert(i,gracz2)
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Wygral: ',gracz2)
        else:
            if wybor2=='a':
                listaWynik.insert(i,gracz2)
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Wygral: ',gracz2)
            elif wybor2=='b':
                listaWynik.insert(i,gracz1)
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Wygral: ',gracz1)
            else :
                listaWynik.insert(i,'Remis')
                print(gracz1," wybiera ",wybor)
                print(gracz2," wybiera ",wybor2)
                print('Remis')
if tryb=='a':
    gracz2 = 'AI'
    for i in range (0,iloscRund):
        wybor = input('Wybierz:\na) kamien\nb) papier\nc) nozyce')
        if(wybor!='a' and wybor!='b' and wybor!='c'):
            while(wybor!='a' and wybor!='b' and wybor!='c'):
                wybor = input('Wybierz:\na) kamien\nb) papier\nc) nozyce')
        wyborAIrand = komputerWybory[random.randint(0,2)]
        if wybor=='a' :
            if wyborAIrand=='kamien':
                listaWynik.insert(i,'Remis')
                print('Remis')
            elif wyborAIrand=='papier':
                listaWynik.insert(i,'AI')
                print('Wygralo AI')
            else :
                listaWynik.insert(i,gracz1)
                print('Wygral: ',gracz1)
        elif wybor=='b' :
            if wyborAIrand=='kamien':
                listaWynik.insert(i,gracz1)
                print('Wygral: ',gracz1)
            elif wyborAIrand=='papier':
                listaWynik.insert(i,'Remis')
                print('Remis')
            else :
                listaWynik.insert(i,'AI')
                print('Wygralo AI')
        else:
            if wyborAIrand=='kamien':
                listaWynik.insert(i,'AI')
                print('Wygralo AI')
            elif wyborAIrand=='papier':
                listaWynik.insert(i,gracz1)
                print('Wygral: ',gracz1)
            else :
                listaWynik.insert(i,'Remis')
                print('Remis')
print(listaWynik)
zliczenieGracza1 = 0
zliczeniePrzeciwnika = 0
remisy = 0
for i in listaWynik :
    if i == gracz1 :
        zliczenieGracza1+=1
    elif i == gracz2:
        zliczeniePrzeciwnika+=1
    else:
        remisy+=1
if zliczenieGracza1 > zliczeniePrzeciwnika:
    if zliczenieGracza1 >= remisy:
        print("Wygral ",gracz1)
    else:
        print("Remis")
elif(zliczeniePrzeciwnika>zliczenieGracza1):
    if(zliczeniePrzeciwnika>=remisy):
        print("Wygral ",gracz2)
    else:
        print("Remis")
else:
    print("Remis")