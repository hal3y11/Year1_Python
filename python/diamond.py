def diamond(width):
    if 2 <= width <= 40:
        for row in range(1, width, 2):
            print(" " * ((width - row) // 2) + "*" * row)
        for column in range(width, 0, -2):
            print(" " * ((width - column) // 2) + "*" * column)
    else:
        print("Width should be between 2 and 40. Please enter a valid width.")
        
width = int(input("Enter the width of the diamond (between 2 and 40): "))
diamond(width)
