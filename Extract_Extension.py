import os

def extract_extension(file_name):
    return os.path.splitext(file_name)[1]

# Example usage
print(extract_extension("example.txt"))  # Output: ".txt"