def character_print(char, num_times):
    for i in range(num_times):
        print(char)

num = int(input("Enter a positive number: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    text_char = input("Enter a text character: ")
    character_print(text_char, num)