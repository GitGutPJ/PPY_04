import random
listaMiast = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań","Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
for i in range(0,10):
    liczba = random.randint(0,len(listaMiast)-1)
    print(i,'.  ',listaMiast.pop(liczba))
