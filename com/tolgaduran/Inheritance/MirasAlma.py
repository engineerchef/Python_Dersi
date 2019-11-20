class Vehicle():
    def __init__(self, numberOfWheel: int, numberOfDoor: int):
        self.numberOfWheel = numberOfWheel
        self.numberOfDoor = numberOfDoor

    def openDoor(self):
        print("Door Opened!")


class LongVehicle(Vehicle):
    def __init__(self, numberOfWheel, numberOfDoor, numberOfTurbo):
        super().__init__(numberOfWheel, numberOfDoor)
        self.numberOfTurbo = numberOfTurbo

    def leaveDodge(self):
        print("Dodge left!")


LV = LongVehicle(8, 2, 2)
print(LV.numberOfDoor)
print(LV.numberOfWheel)
print(LV.numberOfTurbo)