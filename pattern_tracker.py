def find_occurrences(text, pattern):
        positions = []
        for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                        positions.append(i)
        count = len(positions)
        if count > 0:
                return(True, count, positions)
        else:
                return (False, 0, [])
text = input("Enter the text to be analyzed: ")
pattern = input("Enter the pattern to be searched:")
boolean, occurrences, positions = find_occurrences(text, pattern)
print(f"Was the pattern found?  {boolean}.")
print(f"How many times the pattern was found?  {occurrences}.")
print(f"What are the positions within the string? {positions}")