class Car:
    inventory = []

    # initializer with instance attributes
    def __init__(self, make, model, vin, mileage, price, features):
        self.make = make
        self.model = model
        self.vin = vin
        self.mileage = mileage
        self.price = price
        self.features = features

    # adds a new car to the inventory list
    def add_car(self):
        Car.inventory.append(self)

    # sets an attribute to a new value
    def edit_car(self, attribute):
        if attribute == "features":
            self.features = input("Enter new features: ").split(", ")
        else:
            setattr(self, attribute, input(f"Enter new {attribute}: "))

    # displays an individual car
    def display_car(self):
        print(
            f"Make: {self.make}, Model: {self.model}, VIN: {self.vin}, Mileage: {self.mileage}, Price: ${self.price}, Features: {self.features}"
        )

    # deletes a car from the inventory list
    def delete_car(self):
        Car.inventory.remove(self)

    # displays all cars in the inventory list
    def display_inventory():
        for num, car in enumerate(Car.inventory, start=1):
            print(
                f"{num}. Make: {car.make}, Model: {car.model}, VIN: {car.vin}, Mileage: {car.mileage}, Price: ${car.price}, Features: {car.features}"
            )


def main():
    print("\nInventory Tracker")
    print("================")
    print("1. Add a car")
    print("2. Edit a car")
    print("3. Delete a car")
    print("4. Display inventory")
    print("5. Save inventory data")
    print("6. Load inventory data")
    print("7. Exit")

    input_option = int(input("Please select an option: "))
    if input_option == 1:
        print("\nAdd a car")
        print("================")
        # get user input for car attributes
        make = input("Make: ")
        model = input("Model: ")
        vin = input("VIN: ")
        mileage = input("Mileage: ")
        price = input("Price: ")
        features = input("Features: ").split(", ")
        # create a new car object
        new_car = Car(make, model, vin, mileage, price, features)
        # add the new car to the inventory list
        new_car.add_car()
        print("\nUpdated inventory:")
        Car.display_inventory()
        continue_program()

    elif input_option == 2:
        print("\nEdit a car")
        print("================")
        Car.display_inventory()
        # get user input for car attributes
        car_to_edit = int(input("Enter the number of the car you would like to edit: "))
        attribute = input("Enter the attribute you would like to edit: ").lower()
        # get the car object from the inventory list
        # set the attribute to the new value
        Car.inventory[car_to_edit - 1].edit_car(attribute)
        # display the updated car
        print("\nUpdated vehicle info:")
        Car.inventory[car_to_edit - 1].display_car()
        continue_program()

    elif input_option == 3:
        print("\nDelete a car")
        print("================")
        Car.display_inventory()
        car_to_delete = int(
            input("Enter the number of the car you would like to delete: ")
        )
        # get the car object from the inventory list
        # delete the car from the inventory list
        Car.inventory[car_to_delete - 1].delete_car()
        # display the updated inventory
        print("\nUpdated inventory:")
        Car.display_inventory()
        continue_program()

    elif input_option == 4:
        print("\nDisplay inventory")
        print("================")
        Car.display_inventory()
        continue_program()

    elif input_option == 5:
        textfile = open("inventory.txt", "w")
        for car in Car.inventory:
            textfile.write(
                f"{car.make}, {car.model}, {car.vin}, {car.mileage}, {car.price}, {car.features}\n"
            )
        textfile.close()
        print("\nInventory data saved.")
        continue_program()

    elif input_option == 6:
        textfile = open("inventory.txt", "r")
        for line in textfile:
            line = line.strip().split(", ")
            make = line[0]
            model = line[1]
            vin = line[2]
            mileage = line[3]
            price = line[4]
            features = line[5:]
            new_car = Car(make, model, vin, mileage, price, features)
            new_car.add_car()
        textfile.close()
        print("\nInventory data loaded.")
        continue_program()

    elif input_option == 7:
        print("Exiting...")


def continue_program():
    continue_option = input("\nPress any key to continue or 'q' to quit: ")
    if continue_option == "q":
        print("Exiting...")
    else:
        main()

main()
