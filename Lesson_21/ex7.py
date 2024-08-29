#Write a function that swaps the values of two tuples.

def swap_tuples(tuple1, tuple2):
    return tuple2, tuple1

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
swapped = swap_tuples(tuple1, tuple2)
print("Swapped tuples:", swapped)
