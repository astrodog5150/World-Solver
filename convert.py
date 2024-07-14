import json
from wordlistbig import wordlist

# Define the output JSON file name
output_file = 'wordlistbig.json'

# Write the wordlist to the JSON file
with open(output_file, 'w') as f:
    json.dump({'wordlist': wordlist}, f, indent=4)

print(f"Wordlist has been written to {output_file}")