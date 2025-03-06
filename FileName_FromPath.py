import os

def get_file_name(file_path):
    return os.path.basename(file_path)

# Example usage
print(get_file_name("/path/to/example.txt"))  # Output: "example.txt"