from datetime import datetime


class Szoba:
    def __init__(self, szobaszam, tipus, ar):
        self.szobaszam = szobaszam
        self.tipus = tipus
        self.ar = ar


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szobaszam, tipus, ar):
        self.szobak.append(Szoba(szobaszam, tipus, ar))

    def foglalas(self, foglalas):
        self.foglalasok.append(foglalas)

    def osszes_foglalas_ar(self):
        osszes_ar = sum([szoba.ar for szoba in self.szobak])
        print(f"A foglalások összesen {osszes_ar} Ft-ba kerülnek.")

    def osszes_szoba_listazasa(self):
        print("Elérhető szobák:")
        for szoba in self.szobak:
            print(f"{szoba.szobaszam} - {szoba.tipus} - {szoba.ar} Ft/éj")

    def szabad_szobak(self, datum):
        foglalt_szobak = [foglalas.szobaszam for foglalas in self.foglalasok if foglalas.datum == datum]
        return [szoba for szoba in self.szobak if szoba.szobaszam not in foglalt_szobak]

    def foglalas_torlese(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print("Foglalása sikeresen törölve!")
                return
        print("Nincs ilyen foglalás.")

    def osszes_foglalas_listazasa(self):
        print("Foglalások:")
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas.szobaszam}, Dátum: {foglalas.datum.strftime('%Y.%m.%d')}")


class UI:
    @staticmethod
    def foglalas_felvetele(szalloda):
        print("Foglalás felvétele")
        datum_input = input("Adja meg a kívánt dátumot (YYYY.MM.DD formátumban): ")
        try:
            datum_obj = datetime.strptime(datum_input, "%Y.%m.%d")
            if datum_obj < datetime.now():
                print("Múltbeli dátumot nem lehet megadni!")
                return
            szabad_szobak = szalloda.szabad_szobak(datum_obj)
            if szabad_szobak:
                print("Elérhető szobák ezen a dátumon:")
                for szoba in szabad_szobak:
                    print(f"{szoba.szobaszam} - {szoba.tipus} - {szoba.ar} Ft/éj")
                szobaszam = input("Válasszon egy szobát: ")
                for szoba in szabad_szobak:
                    if szoba.szobaszam == szobaszam:
                        foglalas_ar = szoba.ar
                        break
                else:
                    print("Érvénytelen szobaszám.")
                    return

                foglalas = Foglalas(szobaszam, datum_obj)
                szalloda.foglalas(foglalas)
                print(f"Foglalás sikeresen rögzítve! Összesen fizetendő: {foglalas_ar} Ft")
            else:
                print("A megadott dátumra nincs szabad szoba. Kérem válasszon másik dátumot!")
        except ValueError:
            print("Érvénytelen dátum formátum!")

    @staticmethod
    def foglalas_leadasa(szalloda):
        print("Foglalás lemondása")
        foglalas_szobaszam = input("Adja meg a lemondani kívánt foglalás szobaszámát: ")
        foglalas_datum = input("Adja meg a lemondani kívánt dátumot (YYYY.MM.DD formátumban): ")
        try:
            foglalas_datum_obj = datetime.strptime(foglalas_datum, "%Y.%m.%d")
            szalloda.foglalas_torlese(foglalas_szobaszam, foglalas_datum_obj)
        except ValueError:
            print("Érvénytelen dátum formátum!")

    @staticmethod
    def osszes_szoba_listazasa(szalloda):
        szalloda.osszes_szoba_listazasa()

    @staticmethod
    def osszes_foglalas_listazasa(szalloda):
        szalloda.osszes_foglalas_listazasa()


class Foglalas:
    def __init__(self, szobaszam, datum):
        self.szobaszam = szobaszam
        self.datum = datum


def main():
    szalloda = Szalloda("The Potato Hotel")

    # Szobák hozzáadása
    szalloda.add_szoba("101", "Egyágyas szoba", 8000)
    szalloda.add_szoba("201", "Kétágyas szoba", 12000)
    szalloda.add_szoba("301", "Luxus lakosztály", 32000)

    # Foglalások hozzáadása
    szalloda.foglalas(Foglalas("101", datetime(2024, 5, 15)))
    szalloda.foglalas(Foglalas("101", datetime(2024, 5, 16)))
    szalloda.foglalas(Foglalas("201", datetime(2024, 6, 15)))
    szalloda.foglalas(Foglalas("301", datetime(2024, 7, 17)))
    szalloda.foglalas(Foglalas("301", datetime(2024, 9, 18)))

    while True:
        print("\nVálassz egy műveletet:")
        print("1. Foglalás megkezdése")
        print("2. Foglalás lemondása")
        print("3. Elérhető szobák listázása")
        print("4. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Válasszon az alábbi műveletek közül: ")

        if valasztas == "1":
            UI.foglalas_felvetele(szalloda)
        elif valasztas == "2":
            UI.foglalas_leadasa(szalloda)
        elif valasztas == "3":
            UI.osszes_szoba_listazasa(szalloda)
        elif valasztas == "4":
            UI.osszes_foglalas_listazasa(szalloda)
        elif valasztas == "0":
            break
        else:
            print("A kiválaszott lehetőség nem létezik. Kérlek, válassz a megadott lehetőségek közül.")


if __name__ == "__main__":
    main()
