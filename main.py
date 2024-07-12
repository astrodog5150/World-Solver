from wordlistbig import wordlist


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
    return [word for word in words if all(word[pos] == letter for pos, letter in position_dict.items())]

#filter by not letter position
def filter_words_not_in_position(words, not_position_dict):
    return [word for word in words if all(word[pos] != letter for pos, letter in not_position_dict.items())]

# Example usage
desired_length = 5
exclude_letters = {}
include_letters = {}
position_dict = {}
not_position_dict = {}



#creating list
# First filter by length
filtered_words_by_length = filter_words_by_length(wordlist, desired_length)

# Then filter by excluding letters
filtered_words_excluding = filter_words_excluding_letters(filtered_words_by_length, exclude_letters)

# Then filter by including letters
filtered_words_including = filter_words_including_letters(filtered_words_excluding, include_letters)

# Finally filter by specific positions
filtered_words_by_position = filter_words_by_position(filtered_words_including, position_dict)

#Filter by not specific positions
final_list = filter_words_not_in_position(filtered_words_by_position, not_position_dict)

# Print the filtered list of words
print(len(final_list))