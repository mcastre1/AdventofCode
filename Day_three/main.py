DIRECTIONS = [[-1,-1],[-1,0],[-1,1],
              [0,-1],         [0,1],
              [1,-1], [1,0],[1,1]]

SEEN = []

def is_Int(a):
    try:
        temp = int(a)
        return True
    except:
        return False
    
def findNumber(row, col_start, lines):
    temp_col = col_start
    num = ""
    num += lines[row][temp_col]
    SEEN.append(f"{row}, {temp_col}")

    while True:
        if temp_col == len(lines[0]) - 1:
            break

        if not is_Int(lines[row][temp_col + 1]):
            break
        else:
            temp_col += 1
            num += lines[row][temp_col]
            SEEN.append(f"{row}, {temp_col}")

    return num

        

if __name__ == "__main__":
    lines = []
    sum = 0

    # Turn text file into a multi dimensional array(list of lists.)
    with open("./Day_three/big.txt") as file:
        for line in file:
            lines.append(list(line))

    lines = [line if not line[-1] == "\n" else line[:-1] for line in lines]

    # Iterate and find all symbols
    for row_index, row in enumerate(lines):
        for col_index, val in enumerate(row):
            if not is_Int(val) and not val == '.':
                # Checking all 8 adjacent cells
                for direction in DIRECTIONS:
                    row_dir = direction[0]
                    col_dir = direction[1]

                    # Check if we are at the edge
                    if col_index == 0 and col_dir == -1:
                        continue
                    if row_index == 0 and row_dir == -1:
                        continue
                    if col_index == len(lines[0]) - 1 and col_dir == 1:
                        continue
                    if row_index == len(lines) - 1 and row_dir == 1:
                        continue

                    if is_Int(lines[row_index + row_dir][col_index + col_dir]) and not f"{row_index + row_dir}, {col_index + col_dir}" in SEEN:
                        temp_col = col_index + col_dir

                        while True:
                            if temp_col == 0:
                                sum += int(findNumber(row_index + row_dir, temp_col, lines))
                                break

                            if not is_Int(lines[row_index + row_dir][temp_col - 1]):
                                sum += int(findNumber(row_index + row_dir, temp_col, lines))
                                break
                            else:
                                temp_col-=1

    print(sum)
        




