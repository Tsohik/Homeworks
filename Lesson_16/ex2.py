#Write a function that removes an element at a specified index from a list. Handle the IndexError by raising a custom exception if the index is out of range.

def remove_element_at_index(lst, index):
    try:
        return lst.pop(index)
    except IndexError:
        print(f"Error: Index {index} is out of range.")
my_list = [10, 20, 30, 40, 50]

removed_element = remove_element_at_index(my_list, 2)
if removed_element is not None:
    print(f"Removed element: {removed_element}")
    print(f"Updated list: {my_list}")
remove_element_at_index(my_list, 10)
