import string

def frequency_analysis(ciphertext):
    # Define the alphabet
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    
    # Initialize a dictionary to store the frequency of each letter
    frequency_dict = {char: 0 for char in alphabet}
    
    # Count the frequency of each letter in the ciphertext
    for char in ciphertext:
        if char in frequency_dict:
            frequency_dict[char] += 1
    
    # Sort the letters based on their frequency in descending order
    sorted_letters = sorted(frequency_dict, key=frequency_dict.get, reverse=True)
    
    return sorted_letters

# Example usage:
ciphertext = "Gur dhvpx oebja sbk whzcrq bire gur ynml qbt."
sorted_frequency = frequency_analysis(ciphertext)

print("Ciphertext:", ciphertext)
print("Sorted Frequency:", sorted_frequency)
