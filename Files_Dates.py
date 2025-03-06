import os
import time

def get_file_dates(file_path):
    creation_time = os.path.getctime(file_path)
    modification_time = os.path.getmtime(file_path)
    return time.ctime(creation_time), time.ctime(modification_time)

# Example usage
print(get_file_dates("example.txt"))