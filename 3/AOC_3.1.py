with open("3\input_3.1.txt", "r") as lines:
    lines = lines.readlines()
    
list = [list(line.strip()) for line in lines]


def getWholeNumber(matrix, row, col):
    number = ''

    # left
    for i in range(col, -1, -1):
        if not matrix[row][i].isdigit():
            break
        number = matrix[row][i] + number

    # right
    for i in range(col + 1, len(matrix[row])):
        if not matrix[row][i].isdigit():
            break
        number += matrix[row][i]

    return number

def findPartNumbers(matrix, row, col):
    partNumbers = set()
    # above
    if row > 0 and matrix[row -1 ][col].isdigit():
        partNumbers.add(getWholeNumber(matrix, row - 1, col))

    # below
    if row < len(matrix) - 1 and matrix[row +1 ][col].isdigit():
        partNumbers.add(getWholeNumber(matrix, row + 1, col))

    # left
    if col > 0 and matrix[row][col -1].isdigit():
        partNumbers.add(getWholeNumber(matrix, row, col - 1))

    # right
    if col < len(matrix[row]) - 1 and matrix[row][col+1].isdigit():
        partNumbers.add(getWholeNumber(matrix, row, col + 1))

    # top left
    i, j = row, col
    while i > 0 and j > 0 and matrix[i - 1][j - 1].isdigit():
        i -= 1
        j -= 1
        if matrix[i][j].isdigit():
            partNumbers.add(getWholeNumber(matrix, i, j))

    # top right
    i, j = row, col
    while i > 0 and j < len(matrix[row]) - 1 and matrix[i - 1][j + 1].isdigit():
        i -= 1
        j += 1
        if matrix[i][j].isdigit():
            partNumbers.add(getWholeNumber(matrix, i, j))

    # bottom left
    i, j = row, col
    while i < len(matrix) - 1 and j > 0 and matrix[i + 1][j - 1].isdigit():
        i += 1
        j -= 1
        if matrix[i][j].isdigit():
            partNumbers.add(getWholeNumber(matrix, i, j))

    # bottom right
    i, j = row, col
    while i < len(matrix) - 1 and j < len(matrix[row]) - 1 and matrix[i + 1][j + 1].isdigit():
        i += 1
        j += 1
        if matrix[i][j].isdigit():
            partNumbers.add(getWholeNumber(matrix, i, j))

    partNumbers = [num for num in partNumbers if num]

    return partNumbers

totalSum = 0

for rowId, row in enumerate(list):
    for colId, char in enumerate(row):
        if char != '.' and not char.isdigit():
            partNumbers = findPartNumbers(list, rowId, colId)

            if partNumbers:
                totalSum += sum(map(int, partNumbers))

print(f"Total sum: {totalSum}")