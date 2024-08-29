# Given two dictionaries, merge them into a new dictionary, excluding any keys that start with an underscore.


dict1 = {"a":1, "_b":6, "b": 2}
dict2 = {"c":3, "_d":8, "d":4}
merged_dict = {k: v for d in (dict1, dict2) for k, v in d.items() if not k.startswith("_")}
print(merged_dict)
