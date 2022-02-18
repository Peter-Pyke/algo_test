import cost_data
from Facility import Facility
from Customers import Customer

f1 = Facility(1, 17391, 7936)
f2 = Facility(2, 122740, 5931)
f3 = Facility(3, 233153, 7499)
f4 = Facility(4, 205967, 9643)
f5 = Facility(5, 234507, 9556)
f6 = Facility(6, 42050, 8585)
f7 = Facility(7, 90581, 11130)
f8 = Facility(8, 230641, 8229)
f9 = Facility(9, 52511, 7316)
f10 = Facility(10, 103429, 11935)

c1 = Customer(1, 2336)
c2 = Customer(2, 1591)
c3 = Customer(3, 858)
c4 = Customer(4, 886)
c5 = Customer(5, 775)
c6 = Customer(6, 2000)
c7 = Customer(7, 1433)
c8 = Customer(8, 885)
c9 = Customer(9, 2409)
c10 = Customer(10, 1146)
c11 = Customer(11, 1837)
c12 = Customer(12, 1219)
c13 = Customer(13, 518)
c14 = Customer(14, 662)
c15 = Customer(15, 741)
c16 = Customer(16, 1898)
c17 = Customer(17, 1228)
c18 = Customer(18, 1554)
c19 = Customer(19, 1054)
c20 = Customer(20, 1819)
c21 = Customer(21, 1513)
c22 = Customer(22, 1314)
c23 = Customer(23, 1012)
c24 = Customer(24, 2391)
c25 = Customer(25, 1718)
c26 = Customer(26, 2340)
c27 = Customer(27, 1434)
c28 = Customer(28, 1175)
c29 = Customer(29, 1297)
c30 = Customer(30, 794)

list_of_open_facilities_in_order = [f3, f8, f5, f4, f2, f10, f7, f9, f6, f1]  # Maybe just manually fill these lists
list_of_customer_with_demand = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14,
                                c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30]
my_cost_matrix = cost_data.load_cost_data("cost_data.txt")

customer_id = list_of_customer_with_demand[0].cust_id
copy_of_list_of_customers = list_of_customer_with_demand.copy()
copy_of_list_of_facilities = list_of_open_facilities_in_order.copy()

while list_of_customer_with_demand:
    for facility in copy_of_list_of_facilities:
        if facility.open:
            if list_of_customer_with_demand:
                lowest_cost = 10000
                lowest_cost_customer = Customer(100, 0)
                for customer in copy_of_list_of_customers:
                    if customer.satisfied or (customer.demand == 0):
                        continue
                    elif lowest_cost > cost_data.get_cost_data(customer.cust_id, facility.facility_id, my_cost_matrix):
                        lowest_cost = cost_data.get_cost_data(customer.cust_id, facility.facility_id, my_cost_matrix)
                        lowest_cost_customer = customer
                if lowest_cost_customer.demand < facility.capacity:
                    current_capacity = facility.capacity - lowest_cost_customer.demand
                    facility.update_facility(current_capacity)
                    lowest_cost_customer.update_demand(lowest_cost_customer.demand)
                    lowest_cost_customer.update_satisfied()
                    list_of_customer_with_demand.remove(lowest_cost_customer)
                elif facility.capacity < lowest_cost_customer:
                    lowest_cost_customer.update_demand(facility.capacity)
                    facility.update_facility(0)
                    list_of_open_facilities_in_order.remove(facility)




