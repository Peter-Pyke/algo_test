def load_cost_data(file_name):
    matrix = []
    with open(file_name) as our_data:
        for row in our_data:
            matrix.append(row.split("\t"))
    return matrix


my_matrix = load_cost_data("cost_data.txt")


def get_cost_data(customer, facility, cost_matrix):
    cost = cost_matrix[facility][customer]
    return cost

