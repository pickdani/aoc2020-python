lines = [x for x in open('input').read().splitlines()]

def solve(lines):

    # read in as 2d array
    grid = []
    for line in lines:
        grid.append(line)

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    ans = 1

    for slope in slopes:
        count = 0
        r = c = 0
        while r < len(grid):
            if grid[r][c % len(grid[0])] == '#':
                count += 1

            r += slope[1]
            c += slope[0]
        ans *= count

    return ans

print(solve(lines))
