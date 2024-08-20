rainbow = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]

no = int(input("Enter an integer from 1 to 7 (-1 to end): "))

if no == -1:
    print("Exiting the program. Goodbye!")
elif 1 <= no <= 7:
    color = rainbow[no - 1]
    print(f"The color corresponding to {no} is {color}.")
else:
    print("Invalid input. Please enter an integer from 1 to 7 or -1 to end the program.")
