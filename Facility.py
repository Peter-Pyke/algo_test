class Facility:
    def __init__(self, facility_id, capacity):
        self.facility_id = facility_id
        self.capacity = capacity
        self.open = True

    def update_facility(self, current_capacity):
        if current_capacity == 0:
            self.open = False
        else:
            self.capacity = current_capacity

