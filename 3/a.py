lines = [x for x in open('input').read().splitlines()]

def solve(lines):

    # read in as 2d array
    grid = []
    for line in lines:
        grid.append(line)

    r = c = 0
    ans = 0
    while r < len(grid):
        if grid[r][c % len(grid[0])] == '#':
            ans += 1

        r = r + 1
        c = c + 3

    return ans

print(solve(lines))
