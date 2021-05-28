import requests
link = 'http://api.nbp.pl/api/exchangerates/tables/a/'
waluty = requests.get(link).json()[0]['rates']
listaWalut = [i['code'] for i in waluty]
while True:
    hajs = float(input("Wprowadź ilość pieniędzy w PLN, którą chcesz przeliczyć : " ))
    waluta = input(f"Jaką walutę chcesz przeliczyć: ({' '.join(listaWalut)}: ").upper()
    if waluta in listaWalut:
        for i in waluty:
            if i['code'] == waluta:
                wynik = round(hajs / i['mid'], 2)
                print(f"{hajs} PLN to {wynik} {i['code']}")
    else:
        print("Niepoprawna nazwa waluty, spróbuj jeszcze raz")