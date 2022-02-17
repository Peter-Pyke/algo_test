class Facility:
    def __init__(self, facility_id, fixed_cost, capacity):
        self.facility_id = facility_id
        self.fixed_cost = fixed_cost
        self.capacity = capacity
        self.open = True

    def update_facility(self, current_capacity):
        if current_capacity == 0:
            self.open = False
        else:
            self.capacity = current_capacity







