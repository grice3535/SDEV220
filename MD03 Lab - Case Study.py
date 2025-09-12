class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

car_input = str(input("Please click Y if you would like to enter vehicle information(Enter XXX to exit): "))

while True:
    if car_input.lower() == 'y':
        vehicle_type = str(input("Enter vehicle type: "))
        year = int(input("Enter vehicle year: "))
        make = str(input("Enter vehicle make: "))
        model = str(input("Enter vehicle model: "))
        doors = int(input("Enter number of doors: "))
        roof = str(input("Enter type of roof (e.g., sunroof, hardtop): "))

        automobile = Automobile(vehicle_type, year, make, model, doors, roof)

        print("\nVehicle Information:")
        print(f"Type: {automobile.vehicle_type}")
        print(f"Year: {automobile.year}")
        print(f"Make: {automobile.make}")
        print(f"Model: {automobile.model}")
        print(f"Number of Doors: {automobile.doors}")
        print(f"Type of Roof: {automobile.roof}\n")

        car_input = str(input("Please click Y if you would like to enter vehicle information(Enter XXX to exit): "))
    elif car_input.lower() == 'xxx':
        print("Exiting the program.")
        break
    else:
        car_input = str(input("Invalid input. Please click Y to enter vehicle information or XXX to exit: "))
       