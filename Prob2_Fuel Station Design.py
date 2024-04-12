class FuelStation:
    def __init__(self, diesel, petrol, electric):
        self.initial_slots = {"diesel": diesel, "petrol": petrol, "electric": electric}
        self.slots = self.initial_slots.copy()

    def fuel_vehicle(self, fuel_type):
        if self.slots[fuel_type] > 0:
            self.slots[fuel_type] -= 1
            return True
        else:
            return False

    def open_fuel_slot(self, fuel_type):
        if self.slots[fuel_type] < self.initial_slots[fuel_type]:
            self.slots[fuel_type] += 1
            return True
        else:
            return False

    def capacity(self, fuel_type):
        return self.slots[fuel_type]

# Test the FuelStation class
fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))  # Output: True
print(fuel_station.fuel_vehicle("petrol"))  # Output: True
print(fuel_station.fuel_vehicle("diesel"))  # Output: True
print(fuel_station.fuel_vehicle("electric"))  # Output: True
print(fuel_station.fuel_vehicle("diesel"))  # Output: False
print(fuel_station.open_fuel_slot("diesel"))  # Output: True
print(fuel_station.fuel_vehicle("diesel"))  # Output: True
print(fuel_station.open_fuel_slot("electric"))  # Output: True
print(fuel_station.open_fuel_slot("electric"))  # Output: False
