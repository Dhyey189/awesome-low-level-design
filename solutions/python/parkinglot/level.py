from typing import List
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import VehicleType

class Level:
    def __init__(self, floor: int, car_spots_num: int, truck_spots_num: int = 0, motor_cycle_spots_num: int = 0):
        self.floor = floor
        self.car_spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(car_spots_num)]
        self.truck_spots: List[ParkingSpot] = [ParkingSpot(i, VehicleType.TRUCK) for i in range(truck_spots_num)]
        self.motor_cycle_spots: List[ParkingSpot] = [ParkingSpot(i, VehicleType.MOTORCYCLE) for i in range(motor_cycle_spots_num)]

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        spots = self.car_spots
        if vehicle.get_type() == VehicleType.TRUCK:
            spots = self.truck_spots
        elif vehicle.get_type() == VehicleType.MOTORCYCLE:
            spots = self.motor_cycle_spots

        for spot in spots:
            if spot.is_available():
                spot.park_vehicle(vehicle)
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        spots = self.car_spots
        if vehicle.get_type() == VehicleType.TRUCK:
            spots = self.truck_spots
        elif vehicle.get_type() == VehicleType.MOTORCYCLE:
            spots = self.motor_cycle_spots

        for spot in spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False

    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.car_spots:
            print(f"Car Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}")

        for spot in self.truck_spots:
            print(f"Truck Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}")

        for spot in self.motor_cycle_spots:
            print(f"Moto Cycle Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}")