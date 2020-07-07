# Define Grid
grid = [
    ["G", "G", "B", "R"], 
    ["G", "B", "R", "B"], 
    ["R", "B", "B", "B"]
]

# Capture Results
highest = {
    "color": "",
    "count": 0
}

# Compute Result
iterated = {}

def main():
    for row in range(len(grid) - 1):
        for col in range(len(grid[row]) - 1):
            # Check if column has already been iterated over
            if "R" + str(row) + "C" + str(col) in iterated:
                continue

            # Declare Stack
            stack = []
            count = 1

            # Push on the first cell
            stack.append({
                "row": row,
                "col": col
            })
            iterated["R" + str(row) + "C" + str(col)] = True

            while len(stack) > 0:
                current = stack.pop()
                results = find_neighbors(current['row'], current['col'], grid[row][col])
                stack += results
                count += len(results)
            
            if highest["count"] < count:
                highest['color'] = grid[row][col]
                highest['count'] = count
                

def find_neighbors(row, col, color):
    results = []

    # North
    try:
        if grid[row - 1][col] == color and "R" + str(row - 1) + "C" + str(col) not in iterated:
            iterated["R" + str(row - 1) + "C" + str(col)] = True
            results.append({
                "row": row - 1,
                "col": col
            })
    except IndexError:
        pass

    # South
    try:
        if grid[row + 1][col] == color and "R" + str(row + 1) + "C" + str(col) not in iterated:
            iterated["R" + str(row + 1) + "C" + str(col)] = True
            results.append({
                "row": row + 1,
                "col": col
            })
    except IndexError:
        pass

    # East
    try:
        if grid[row][col + 1] == color and "R" + str(row) + "C" + str(col + 1) not in iterated:
            iterated["R" + str(row) + "C" + str(col + 1)] = True
            results.append({
                "row": row,
                "col": col + 1
            })
    except IndexError:
        pass

    # West
    try:
        if grid[row][col - 1] == color and "R" + str(row) + "C" + str(col - 1) not in iterated:
            iterated["R" + str(row) + "C" + str(col - 1)] = True
            results.append({
                "row": row,
                "col": col - 1
            })
    except IndexError:
        pass

    return results

main()

# Output Results
print('The highest color is {} with a count of {}'.format(highest['color'], highest['count']))