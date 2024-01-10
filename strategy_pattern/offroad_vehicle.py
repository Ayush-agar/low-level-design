from strategy.sports_drive_strategy import SportsDriveStrategy
from vehicle import Vehicle

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(drive_obj=SportsDriveStrategy())
