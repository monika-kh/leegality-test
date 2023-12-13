class ParkingLot:
    slots = {"A": dict.fromkeys(range(1, 3)), "B": dict.fromkeys(range(3, 5))}

    def _find(self, num=None):
        spot = None
        if not num:
            operator = lambda: is_empty is None
        else:
            operator = lambda: is_empty == num
        for floor, floor_slots in self.slots.items():
            for slot, is_empty in floor_slots.items():

                if operator():
                    spot = floor, slot
                    return spot

    def park(self, number):
        spot = self._find()
        if spot:
            self.slots[spot[0]][spot[1]] = number
        else:
            text = "No Spot Is Available"
            return text

    def find_park(self, number=None):
        return self._find(number)

    def unpark(self, number):
        spot = self.find_park(number)

        self.slots[spot[0]][spot[1]] = None
        print(spot)


if __name__ == "__main__":
    parking_lot = ParkingLot()
    def find_parking():
        num = input("""
1. For Parked vehicle
2. Nearest empty Parking"""
            )
        text = ""
        vehicle_num = None
        if num == "1":
            text = "Vehicle is parked at"
            vehicle_num = input(" enter vehicle number")
        elif num == "2":
            text = "Nearest empty spot at "
        else:
            text = "Invalid choice"
        spot = parking_lot.find_park(vehicle_num) if text else ""
        if not spot:
            text = "vehicle not found"
            spot = ''
        print(text, spot)

    x = True
    while x:
        choice = input(
            """
        1. To Park
        2. Find Parking
        3. Unpark
        0. To Exit the program
    """
        )
        c = choice
        if c == "0":
            x = False
        elif c == "1":
            if  parking_lot.find_park() is None:
                print("No parking slot available")
            else:
                print("nearest parking at", parking_lot.find_park())
                num = input("vehicle numer")
                parking_lot.park(num)
        elif c == "2":
            find_parking()
        elif c == "3":
            num = input("vehicle numer")
            parking_lot.unpark(num)
        else:
            print("Invalid input try again")
print("Exiting")


