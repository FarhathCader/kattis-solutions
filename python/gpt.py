def count_letters(letter_list):
    # Initialize the count dictionary
    counts = {'a': 0, 'c': 0, 't': 0, 'g': 0}

    # Iterate over each letter in the list and update the count
    for letter in letter_list:
        if letter in counts:
            counts[letter] += 1

    return counts

def total_count_difference(list1, list2):
    # Count the letters in each list
    counts1 = count_letters(list1)
    counts2 = count_letters(list2)

    # Compute the total difference in counts
    total_difference = sum(abs(counts1[letter] - counts2[letter]) for letter in counts1)

    return total_difference

# Example usage:
list1 = ['a', 'a', 'c']
list2 = ['a', 'c', 'c']

difference = total_count_difference(list1, list2)
print(difference)
