def find_max(sequinсe):
    current_max = sequince[0]
    for element in sequince:
        if element > current_max:
            current_max = element
    return current_max


def find_min(sequince):
    current_min=sequince[0]
    for element in sequince:
        if element < current_min:
            current_min = element
    return current_min


sequince=[4, 10, 2, 5, -2, 0, 1, -4, 7, 3]

maximum = find_max(sequince)
minimum = find_min(sequince)

print (maximum)
print (minimum)