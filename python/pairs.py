# prepare counters
number_of_guesses = 0
number_of_pairs_found = 0

# prepare the grids
card_grid = [["J", "J", "J", "J"],
            ["Q", "Q", "Q", "Q"],
            ["K", "K", "K", "K"],
            ["A", "A", "A", "A"]]

# see https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
# the next line doesn't work as we expected
# display_grid = [['*'] * 4] * 4
display_grid = [["*", "*", "*", "*"],
                ["*", "*", "*", "*"],
                ["*", "*", "*", "*"],
                ["*", "*", "*", "*"]]

# output the display grid
print("  1 2 3 4")
for x in range(4):
    print(str(x+1) + " ", end='')
    for y in range(4):
        print(display_grid[x][y] + " ", end='')
    print()

# while not all pairs identified do
while number_of_pairs_found < 8:
    number_of_guesses += 1

    # ask the user to select a pair of cards in the grid
    print("Enter co-ordinates of your first choice (x, y) ", end='')
    x1 = int(input('> '))
    y1 = int(input('> '))

    # validate user choice
    while display_grid[x1-1][y1-1] == 'X':
        # ask the user to select a pair of cards in the grid
        print("Not a correct choice, please try again.\nEnter co-ordinates of your first choice (x, y) ", end='')
        x1 = int(input('> '))
        y1 = int(input('> '))

    x1 -= 1
    y1 -= 1
    display_grid[x1][y1] = card_grid[x1][y1]

    # output the display grid showing the chosen card
    print("  1 2 3 4")
    for x in range(4):
        print(str(x+1) + " ", end='')
        for y in range(4):
            print(display_grid[x][y] + " ", end='')
        print()

    print("Enter co-ordinates of your second choice (x, y) ", end='')
    x2 = int(input('> '))
    y2 = int(input('> '))

    # validate user choice
    while display_grid[x2-1][y2-1] == 'X':
        # ask the user to select a pair of cards in the grid
        print("Not a correct choice, please try again.\nEnter co-ordinates of your second choice (x, y) ", end='')
        x2 = int(input('> '))
        y2 = int(input('> '))

    x2 -= 1
    y2 -= 1
    display_grid[x2][y2] = card_grid[x2][y2]

    # output the display grid showing both chosen cards
    print("  1 2 3 4")
    for x in range(4):
        print(str(x) + " ", end='')
        for y in range(4):
            print(display_grid[x][y] + " ", end='')
        print()

    # check the user's selection
    if card_grid[x1][y1] == card_grid[x2][y2]:
        display_grid[x1][y1] = 'X'
        display_grid[x2][y2] = 'X'
        number_of_pairs_found += 1
        print("Congratulations, you have now found", number_of_pairs_found, "pairs")
    else:
        display_grid[x1][y1] = '*'
        display_grid[x2][y2] = '*'
        print("Hard luck! Try again")

    # output the display grid with the results
    print("  1 2 3 4")
    for x in range(4):
        print(str(x+1) + " ", end='')
        for y in range(4):
            print(display_grid[x][y] + " ", end='')
        print()

# display number of guesses needed to complete the grid
print("You took", number_of_guesses, "guesses to find all the pairs")
