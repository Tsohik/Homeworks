#Write a function that returns the nth largest element from a list.

def nth_largest_element(lst, n):
    if n <= 0 or n > len(lst):
        return None
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[n - 1]


numbers = [10, 20, 4, 45, 99]
n = 3
print(f"The {n}rd largest element is: {nth_largest_element(numbers, n)}")
