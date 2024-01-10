from strategy.normal_drive_strategy import NormalDriveStrategy
from vehicle import Vehicle

class GoodsVehicle(Vehicle):
    def __init__(self):
        super().__init__(drive_obj=NormalDriveStrategy())
