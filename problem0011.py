"""PROJECT EULER Problem 11: Python3"""

def main():

    twenty_string = """
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """

    twenty_grid = to_grid(twenty_string)
    #print(twenty_grid)
    row = largest_row(twenty_grid)
    print("largest_row: ", largest_row(twenty_grid))
    column = largest_column(twenty_grid)
    print("largest_column: ", largest_column(twenty_grid))

    right_diaglist = right_diagonals(twenty_grid)
    left_diaglist = left_diagonals(twenty_grid)
    print("largest right diagonal: ", largest_diagonal(right_diaglist))
    print("largest left diagonal: ", largest_diagonal(left_diaglist))

    # pick largest
    largest = 0
    for num in row, column, largest_diagonal(right_diaglist), largest_diagonal(left_diaglist):
        if num[0] > largest:
            largest = num[0]

    print("\n\nlargest product of 4 adjacent numbers in the grid: ", largest)



def to_grid(long_string):
    long_list = long_string.split()
    long_list = list(map(int, long_list))
    long_grid = []
    for j in range(0, 381, 20):
        add_row = long_list[j:(j+20)]
        long_grid.append(add_row)
    return long_grid



def largest_product(number_list):
    """Given a list of numbers, find the greatest product of 4 adjacent numbers.
    Returns a tuple of largest product and the 4 numbers that were involved.
    e.g., (360, [3, 4, 5, 6])"""

    the_largest = 0
    largest_list = []
    list_length = len(number_list)
    adjacent_length = 4
    for j in range(list_length - adjacent_length):
        possible_largest = 1
        possible_list = []
        for i in range(adjacent_length):
            possible_largest *= number_list[j+i]
            possible_list.append(number_list[j+i])

        if possible_largest > the_largest:
            the_largest = possible_largest
            largest_list = possible_list
    return the_largest, largest_list


def largest_row(grid):
    """Given a list of lists (grid) return the largest 4-number product from any of the rows."""

    grid_length = len(grid)
    the_largest = 0
    largest_list = []
    for j in range(grid_length):
        possible = largest_product(grid[j])
        if possible[0] > the_largest:
            the_largest = possible[0]
            largest_list = possible[1]

    return the_largest, largest_list

def extract_column(some_list, column_num):
    return [item[column_num] for item in some_list]

def largest_column(grid):
    """Given a list of lists (grid) return the largest 4-number product from any of the rows."""

    grid_length = len(grid)
    the_largest = 0
    largest_list = []
    for j in range(grid_length):
        column = extract_column(grid, j)
        possible = largest_product(column)
        if possible[0] > the_largest:
            the_largest = possible[0]
            largest_list = possible[1]

    return the_largest, largest_list


def right_diagonals(grid):
    """Given a 20x20 grid (list of lists) extract all possible
    diagonals. Then keep only those which have at least 4 adjacent numbers."""
    length_grid = len(grid)
    diagonal_list = []
    min_length = 4

    # main and bottom diagonals!
    for i in range(length_grid):
        new_list = []
        for j in range(length_grid-i):
            new_list.append(grid[i+j][j])
        diagonal_list.append(new_list)

    # now top diags!
    for i in range(1,length_grid):
        new_list = []
        for j in range(length_grid-i):
            new_list.append(grid[j][i+j])
        diagonal_list.append(new_list)

    final_list = []
    for adjacent_list in diagonal_list:
        if len(adjacent_list) >= min_length:
            final_list.append(adjacent_list)

    return final_list


def left_diagonals(grid):
    """Given a 20x20 grid (list of lists) extract all possible
    diagonals. Then keep only those which have at least 4 adjacent numbers."""
    length_grid = len(grid)
    diagonal_list = []
    min_length = 4

    # main and top diagonals!
    for i in range(length_grid-1, -1,-1):
        new_list = []
        for j in range(i+1):
            new_list.append(grid[j][i-j])
        diagonal_list.append(new_list)

    # now bottom diags!
    for i in range(1, length_grid):
        add_one = 0
        new_list = []
        for j in range(length_grid-1, i-1, -1):
            new_list.append(grid[i+add_one][j])
            add_one += 1
        diagonal_list.append(new_list)

    final_list = []
    for adjacent_list in diagonal_list:
        if len(adjacent_list) >= min_length:
            final_list.append(adjacent_list)

    return final_list

def largest_diagonal(diag_list):
    the_largest = 0
    largest_list = []
    for item in diag_list:
        if largest_product(item)[0] > the_largest:
            the_largest = largest_product(item)[0]
            largest_list = largest_product(item)[1]

    return the_largest, largest_list


####################################################################################################
if __name__ == "__main__":
    main()
