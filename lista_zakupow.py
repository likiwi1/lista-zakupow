print("Lista zakupów")
lista = []

while True:
    produkt = input("Wpisz produkt do listy zakupów (wpisz 'koniec' aby zakończyć): ")
    if produkt.lower() == "koniec":
        break
    lista.append(produkt)

if lista:
    print("Twoja lista zakupów:")
    for produkt in lista:
        print(produkt)
else:
    print("Twoja lista jest pusta.")

print("Chcesz dodac lub usunac z listy?")
wybor = input()

if wybor == "dodac":
    while True:
        produkt = input("Wpisz produkt do dodania do listy zakupów (wpisz 'koniec' aby zakończyć dodawanie): ")
        if produkt.lower() == "koniec":
            break
        lista.append(produkt)

    print("Twoja zaktualizowana lista zakupów:")
    for produkt in lista:
        print(produkt)
elif wybor == "usunac":
    produkt_do_usuniecia = input("Wpisz produkt do usunięcia z listy zakupów: ")
    if produkt_do_usuniecia in lista:
        lista.remove(produkt_do_usuniecia)
        print(f"Produkt {produkt_do_usuniecia} został usunięty z listy zakupów.")
    else:
        print("Nie ma takiego produktu na liście.")
else:
    print("Niepoprawna opcja.")

print(lista)