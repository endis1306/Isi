from datetime import datetime

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    @property
    def is_old(self):
        current_year = datetime.now().year
        return current_year - self.rok_produkcji

    @property
    def is_long_mileage(self):
        return self.przebieg

class Car(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg, marka):
        super().__init__(nazwa, rok_produkcji, przebieg)
        self.marka = marka

    @property
    def is_old(self):
        return super().is_old

    @property
    def is_long_mileage(self):
        return super().is_long_mileage

vehicle = Vehicle("Pojazd A", 2005, 150000)
car = Car("Samochód B", 2000, 350000, "BMW")
car_inheritance = Car("Samochód C", 1990, 250000, "Audi")

print(f"{vehicle.is_old=} && {vehicle.is_long_mileage=}")
print(f"{car.is_old=} && {car.is_long_mileage=}")
print(f"{car_inheritance.is_old=} && {car_inheritance.is_long_mileage=}")


