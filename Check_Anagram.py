def check_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
print(check_anagram("listen", "silent"))  # Output: True