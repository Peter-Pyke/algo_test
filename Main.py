import cost_data

list_of_open_facilities_in_order = []
list_of_customer_with_demain = []
my_cost_matrix = cost_data.load_cost_data("cost_data.txt")

for facility in list_of_open_facilities_in_order:
    if list_of_customer_with_demain:
        break
    for customer in range(29):
        lowest_cost = cost_data.get_cost_data(0, facility.facility_id, my_cost_matrix)  # hold index[0][0] as lowest cost place holder
        next_cost = cost_data.get_cost_data(customer, facility.facility_id, my_cost_matrix)  # cost value as loop iterates
        #  This if statement will replace the place value if a lower one is found during the loop
        if next_cost < lowest_cost:
            lowest_cost = next_cost









