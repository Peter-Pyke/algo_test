
import cost_data
from Facility import Facility
from Customers import Customer
from data_pull import load_cost_data, order_facility_list

# Empty lists to hold our data
number_of_facilities = []
number_of_customers = []
fixed_costs = []
demands = []
capacities = []
transport_costs = []
list_of_facilities = []
list_of_customers = []

# function to load our data from text file to empty lists above
load_cost_data("Sample_Data_tab.txt", number_of_facilities, number_of_customers, fixed_costs,
               demands, capacities, transport_costs)

# loop to create facility list unordered
for i in range(10):
    our_facility = Facility(i+1, int(fixed_costs[0][i]), int(capacities[0][i]))
    list_of_facilities.append(our_facility)

# loop to create customer list
for i in range(30):
    our_customer = Customer(i+1, int(demands[0][i]))
    list_of_customers.append(our_customer)

# function to sort facility list
list_of_facilities_in_order = order_facility_list(list_of_facilities)

# creating a matrix to hold our cost data
my_cost_matrix = transport_costs

# copy of our list to use for the loops
customer_id = list_of_customers[0].cust_id
copy_of_list_of_customers = list_of_customers.copy()
copy_of_list_of_facilities = list_of_facilities_in_order.copy()

# initializing our total transport cost and total fix cost objects
total_transport_cost = 0
total_fix_cost = 0

# empty list to be used to keep track of the facilities we use
facility_used = []

# main algorithm loop
while list_of_customers:
    for facility in copy_of_list_of_facilities:
        facility_used.append(facility)
        if facility.open:
            if list_of_customers:
                lowest_cost = 10000
                lowest_cost_customer = Customer(100, 0)
                for customer in copy_of_list_of_customers:
                    if customer.satisfied or (customer.demand == 0):
                        continue
                    elif lowest_cost > cost_data.get_cost_data(customer.cust_id, facility.facility_id, my_cost_matrix):
                        lowest_cost = cost_data.get_cost_data(customer.cust_id, facility.facility_id, my_cost_matrix)
                        lowest_cost_customer = customer
                total_transport_cost += lowest_cost
                if lowest_cost_customer.demand < facility.capacity:
                    current_capacity = int(facility.capacity) - int(lowest_cost_customer.demand)
                    facility.update_facility(current_capacity)
                    lowest_cost_customer.update_demand(lowest_cost_customer.demand)
                    lowest_cost_customer.update_satisfied()
                    list_of_customers.remove(lowest_cost_customer)
                    break
                elif facility.capacity < lowest_cost_customer.demand:
                    lowest_cost_customer.update_demand(facility.capacity)
                    facility.update_facility(0)
                    list_of_facilities_in_order.remove(facility)

# removing duplicate facilities form out facilities used list
facility_used = list(dict.fromkeys(facility_used))

#  printing the id of each facility used
for facility in facility_used:
    print(facility.facility_id)

# printing the capacity left of each facility used
for facility in facility_used:
    total_fix_cost += facility.fixed_cost
    print(facility.capacity)

# printing total cost
print(total_fix_cost + total_transport_cost)





