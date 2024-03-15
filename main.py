def find_max(sequence):
    current_max = sequence[0]
    for element in sequence:
        if element > current_max:
            current_max = element
    return current_max


def find_min(sequence):
    current_min=sequence[0]
    for element in sequence:
        if element < current_min:
            current_min = element
    return current_min


sequence=[4, 10, 2, 5, -2, 0, 1, -4, 7, 3]

maximum = find_max(sequence)
minimum = find_min(sequence)

print (maximum)
print (minimum)
