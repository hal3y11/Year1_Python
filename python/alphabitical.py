strings = [input(f"Enter string {i+1}: ") for i in range(5)]

strings.sort()

print("Sorted Strings:")
for string in strings:
    print(string)

