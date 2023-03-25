def get_modifications(original_array, updated_array):
    original_set = set(original_array)
    updated_set = set(updated_array)

    # find  new elements
    new_elements = list(updated_set - original_set)

    # find removed elements
    removed_elements = list(original_set - updated_set)

    return new_elements, removed_elements
original_array = [1, 2, 3, 4, 5]
updated_array = [2, 3, 5, 7, 9]

new_elements, removed_elements = get_modifications(original_array, updated_array)

print("New elements:", new_elements)
print("Removed elements:", removed_elements)
