"""number of facilities, number of customers, facilities fixed costs,
 customer demands, facility capacities, transportation costs"""

number_of_facilities = []
number_of_customers = []
facilities_fixed_cost = []
customer_demands = []
facility_capacities = []
transportation_cost = []

"""The following function loops through the file, it uses the boolean values associated with
facilities, customer, fixed_cost ect and the if statement to know if that row of data has been passed.
The way pulling data from a text file works, is it goes to a row and indexes that row by each character
in the string of that row unless you provide a delimiter(in this case we use \t or tab)."""


def load_cost_data(file_name):
    facilities = True
    customers = True
    fixed_cost = True
    demand = True
    capacities = True
    transport_cost = True
    with open(file_name) as our_data:
        for row in our_data:
            if len(row.split("\t")) == 2 and facilities:
                number_of_facilities.append(row.split("\t"))
                facilities = False
            elif len(row.split("\t")) == 2 and customers:
                number_of_customers.append(row.split("\t"))
                customers = False
            elif len(row.split("\t")) == 11 and fixed_cost:
                facilities_fixed_cost.append(row.split("\t"))
                fixed_cost = False
            elif len(row.split("\t")) == 30 and demand:
                customer_demands.append(row.split("\t"))
                demand = False
            elif len(row.split("\t")) == 10 and capacities:
                facility_capacities.append(row.split("\t"))
                capacities = False
            elif len(row.split("\t")) == 30 and transport_cost:
                transportation_cost.append(row.split("\t"))
                transport_cost = False
            else:
                print(len(row.split("\t")))
        print(facilities_fixed_cost)


load_cost_data("Sample_Data_tab.txt")
