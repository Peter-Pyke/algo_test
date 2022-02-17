class Customer:
    def __init__(self, cust_id, demand):
        self.cust_id = cust_id
        self.demand = demand
        self.satisfied = False

    def update_demand(self, amount_satisfied):
        current_demand = self.demand
        self.demand = current_demand - amount_satisfied

    def update_satisfied(self):
        self.satisfied = True
