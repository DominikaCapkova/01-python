import pickle
def vzdialenost(sirkaStart: float, dlzkaStart : float, sirkaCiel: float, dlzkaCiel : float) -> float:
    import math
    polomer = 6371000
    sirkaStart = math.radians(sirkaStart)
    dlzkaStart = math.radians(dlzkaStart)
    sirkaCiel = math.radians(sirkaCiel)
    dlzkaCiel = math.radians(dlzkaCiel)
    rozdielSirok = sirkaCiel - sirkaStart
    rozdielDlzok = dlzkaCiel - dlzkaStart
    a = math.sin(rozdielSirok/2) ** 2 + math.cos(sirkaStart) * math.cos(sirkaCiel) * math.sin(rozdielDlzok / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return polomer * c

suradnice = []
class Gps():
    def prejdenaTrasaXY(self, x, y):
        suradnice.append([x, y])
        self.uloz(suradnice)

    def prejdenaCelaTrasa(self):
        totalDistance = 0
        for i in range(0,len(suradnice) - 1):
            totalDistance += vzdialenost(suradnice[i][0],suradnice[i][1],suradnice[i+1][0],suradnice[i+1][1])
        return totalDistance

    def uloz(self,suradnice):
        with open("suradnice.txt", "wb") as f:
            pickle.dump(suradnice, f)

    def nacitaj(self):
        try:
            with open("suradnice.txt", "rb") as f:
                suradnice = pickle.load(f)
                return suradnice
        except FileNotFoundError:
            raise FileNotFoundError("Subor nie ej vytvoreny.")

line = Gps()

line.prejdenaTrasaXY(48.1357803, 17.108364)
line.prejdenaTrasaXY(48.718983, 21.251835)
line.prejdenaTrasaXY(49.011862, 21.245865)

print(line.prejdenaCelaTrasa())
nacitaj = line.nacitaj()
print(nacitaj)
