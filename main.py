from word_list import wordlist


# print(wordlist)

#making filter functions
# filter length
def filter_words_by_length(words, length):
    return [word for word in words if len(word) == length]

#filter excluded letters
def filter_words_excluding_letters(words, exclude_letters):
    return [word for word in words if not any(letter in word for letter in exclude_letters)]

#filter including letters (not specific location)
def filter_words_including_letters(words, include_letters):
    return [word for word in words if all(letter in word for letter in include_letters)]

#filter by letter positions
def filter_words_by_position(words, position_dict):
    """
    Filters a list of words to include only those that have specific letters at specific positions.
    
    Args:
        words (list of str): The list of words to filter.
        position_dict (dict of int: str): A dictionary where keys are positions (0-indexed) and values are the required letters at those positions.
    
    Returns:
        list of str: A list of words that have the specified letters at the specified positions.
    """
    return [word for word in words if all(word[pos] == letter for pos, letter in position_dict.items())]

# Example usage
desired_length = 5
exclude_letters = {'c', 'r', 'a', 't', 's', 'h', 'n', 'v'}
include_letters = {'e', 'l', 'o'}
position_dict = {1: 'o', 3: 'e', 4: 'l'}


#creating list
# First filter by length
filtered_words_by_length = filter_words_by_length(wordlist, desired_length)

# Then filter by excluding letters
filtered_words_excluding = filter_words_excluding_letters(filtered_words_by_length, exclude_letters)

# Then filter by including letters
filtered_words_including = filter_words_including_letters(filtered_words_excluding, include_letters)

# Finally filter by specific positions
filtered_words_by_position = filter_words_by_position(filtered_words_including, position_dict)

# Print the filtered list of words
print(filtered_words_by_position)