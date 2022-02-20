"""number of facilities, number of customers, facilities fixed costs,
 customer demands, facility capacities, transportation costs"""


"""The following function loops through the file, it uses the boolean values associated with
facilities, customer, fixed_cost ect and the if statement to know if that row of data has been passed.
The way pulling data from a text file works, is it goes to a row and indexes that row by each character
in the string of that row unless you provide a delimiter(in this case we use \t or tab)."""


def load_cost_data(file_name, number_of_facilities, number_of_customers,
                   fixed_costs, demands, capacities, transport_costs):
    facilities = True
    customers = True
    fixed_cost = True
    demand = True
    capacity = True
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
                fixed_costs.append(row.split("\t"))
                fixed_cost = False
            elif len(row.split("\t")) == 30 and demand:
                demands.append(row.split("\t"))
                demand = False
            elif len(row.split("\t")) == 11 and capacity:
                capacities.append(row.split("\t"))
                capacity = False
            elif len(row.split("\t")) == 30:
                transport_costs.append(row.split("\t"))
            else:
                print(len(row.split("\t")))


def order_facility_list(list_of_facilities):
    dictionary_of_numbers = {}
    list_in_order_just_facilities = []
    for facility in list_of_facilities:
        number_to_order_by = int(facility.fixed_cost)/int(facility.capacity)
        dictionary_of_numbers[number_to_order_by] = facility
    list_in_order_keys = sorted(dictionary_of_numbers.items())
    for items in list_in_order_keys:
        facility = items[1]
        list_in_order_just_facilities.append(facility)

    return list_in_order_just_facilities