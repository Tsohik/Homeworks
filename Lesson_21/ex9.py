#Write a function that finds the key with the maximum value in a dictionary.

def find_key_with_max_value(d):

    if not d:
        return None
    return max(d, key=d.get)

sample_dict = {
    "apple": 10,
    "banana": 25,
    "cherry": 15,
    "date": 30
}

max_key = find_key_with_max_value(sample_dict)
print(f"The key with the maximum value is: {max_key}")
