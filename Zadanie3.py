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
    choice = getpass.getpass('wybor')
    print('choice')
    gracz2 = input('Nazwij gracza 2')
    for i in range (0,iloscRund+1):
        wybor = input('Wybierz:\na) kamien\nb) papier\nc) nozyce')
        wybor2 = input('Wybierz:\na) kamien\nb) papier\nc) nozyce')
        while(wybor!='a' and wybor!='b' and wybor!='c' and wybor2!='a' and wybor2!='b' and wybor2!='c'):
            if(wybor!='a' and wybor!='b' and wybor!='c'):
                wybor = input('Wybierz:\na) kamien\nb) papier\nc) nozyce')
            else:
                wybor2 = input('Wybierz:\na) kamien\nb) papier\nc) nozyce')
        if wybor=='a' :
            if wybor2=='a':
                listaWynik.insert(i,'Remis')
                print('Remis')
            elif wybor2=='b':
                listaWynik.insert(i,gracz2)
                print('Wygralo: ',gracz2)
            else :
                listaWynik.insert(i,gracz1)
                print('Wygral: ',gracz1)
        elif wybor=='b' :
            if wybor2=='a':
                listaWynik.insert(i,gracz1)
                print('Wygral: ',gracz1)
            elif wybor2=='b':
                listaWynik.insert(i,'Remis')
                print('Remis')
            else :
                listaWynik.insert(i,gracz2)
                print('Wygralo: ',gracz2)
        else:
            if wybor2=='a':
                listaWynik.insert(i,gracz2)
                print('Wygral: ',gracz2)
            elif wybor2=='b':
                listaWynik.insert(i,gracz1)
                print('Wygral: ',gracz1)
            else :
                listaWynik.insert(i,'Remis')
                print('Remis')
if tryb=='a':
    for i in range (0,iloscRund+1):
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