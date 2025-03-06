def lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example usage
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(lists_to_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}