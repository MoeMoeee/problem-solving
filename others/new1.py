def solution(array, row, column, replace):
    start_val = array[row][column]
    rows, cols = len(array), len(array[0])

    def fill(r, c):
        # If the current cell is out of bounds or its value is not the original value, return
        if r < 0 or c < 0 or r >= rows or c >= cols or array[r][c] != start_val:
            return

        # Replace the value at the current cell with the new value
        array[r][c] = replace

        # Recursively fill the neighbors
        fill(r + 1, c)  # down
        fill(r - 1, c)  # up
        fill(r, c + 1)  # right
        fill(r, c - 1)  # left

    fill(row, column)
    return array