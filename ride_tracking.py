# ride_tracking.py
class Ride:
    def __init__(self, ride_id, driver_id, passenger_id, pickup_location, dropoff_location, status="In Progress"):
        self.ride_id = ride_id
        self.driver_id = driver_id
        self.passenger_id = passenger_id
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.status = status