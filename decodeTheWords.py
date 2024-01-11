import re

# Initialize a dictionary
wordCode = {}

with open("/Users/richardjohn/Desktop/CodingChallenges/message_file.txt", "r") as file:
    for line in file:
        code = line.split()
        if len(code) >= 2:
            number = code[0]
            word = code[1]
            wordCode[int(number)] = word

pattern = r'\b\d+\b'

decodedString = ""  # Initialize as a list

input_data = [
    "1",
    "2 3",
    "4 5 6",
]

for line in input_data:
    nums = re.findall(pattern, line)
    if nums:  # Check if there are any numbers in the line
        lastNum = int(nums[-1])
        decodedString += (wordCode.get(lastNum, ""))  # Use get to handle missing keys
        decodedString += " "

print(decodedString)