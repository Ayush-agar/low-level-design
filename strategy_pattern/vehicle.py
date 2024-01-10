from strategy.drive_strategy import DriveStrategy

class Vehicle:
    def __init__(self, drive_obj: DriveStrategy) -> None:
        self.drive_obj = drive_obj

    def drive(self):
        self.drive_obj.drive()
