def find_max(sequenсe):
    current_max = sequenсe[0]
    for element in sequenсe:
        if element > current_max:
            current_max = element
    return current_max


def find_min(sequenсe):
    current_min=sequenсe[0]
    for element in sequenсe:
        if element < current_min:
            current_min = element
    return current_min


sequenсe=[4, 10, 2, 5, -2, 0, 1, -4, 7, 3]

maximum = find_max(sequenсe)
minimum = find_min(sequenсe)

print (maximum)
print (minimum)
