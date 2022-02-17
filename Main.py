import cost_data

list_of_open_facilities_in_order = []  # Maybe just manually fill these lists
list_of_customer_with_demain = []
my_cost_matrix = cost_data.load_cost_data("cost_data.txt")


for facility in list_of_open_facilities_in_order:
    #  Check if we still have customers with demand
    if list_of_customer_with_demain:
        break
    #  Check the cost of each customer for current facility
    for customer in range(29):
        lowest_cost = cost_data.get_cost_data(0, facility.facility_id, my_cost_matrix)  # hold index[0][0] as lowest cost place holder
        next_cost = cost_data.get_cost_data(customer, facility.facility_id, my_cost_matrix)  # cost value as loop iterates
        #  This if statement will replace the place value if a lower one is found during the loop
        if next_cost < lowest_cost:
            lowest_cost = next_cost
    # Find customer with lowest cost
    for row in my_cost_matrix:
        for column in my_cost_matrix:
            if lowest_cost == my_cost_matrix[row][column]:
                lowest_cost_customer_id = column
    #  customer_object and customer_demand is just to simplify below if statements
    customer_object = list_of_customer_with_demain[lowest_cost_customer_id]
    customer_demand = list_of_customer_with_demain[lowest_cost_customer_id].gettattribute("demand")
    #  Check to see if the facility can full satisfy the customer if so update facility capacity and customer demand
    if customer_demand < facility.capacity:
        current_capacity = facility.capacity - customer_demand
        facility.update_facility(current_capacity)
        customer_object.update_demand(customer_demand)
        customer_object.update_satisfied()
        list_of_customer_with_demain.remove(customer_object)
    #  If facility cant fully satisfy demand give what it can to the customer and up date both
    elif facility.capacity < customer_demand:
        customer_object.update_demand(facility.capacity)
        facility.update_facility(0)
        list_of_open_facilities_in_order.remove(facility)









