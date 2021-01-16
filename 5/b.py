lines = [x.strip() for x in open('input').read().splitlines()]

def solve(lines):
    ids = {} # map (r,c) to id
    for line in lines:
        # find row
        lo = 0
        hi = 127

        for c in line[:7]:
            m = (lo + hi) // 2

            if c == 'F': # take lower half
                hi = m

            if c == 'B': # take upp half
                lo = m + 1

        if line[:7].endswith('F'):
            row = hi
        else:
            row = lo

        # find col
        lo = 0
        hi = 7
        for r in line[7:]:
            m = (lo + hi) // 2

            if r == 'L':
                hi = m

            if r == 'R':
                lo = m + 1

        if line[7:].endswith('R'):
            col = lo
        else:
            col = hi

        pid = row * 8 + col

        ids[(row, col)] = pid

    allid = ids.values()

    for r in range(1, 127): # exclude first and last row
        for c in range(8):
            cid = r * 8 + c
            # find id missing
            if cid + 1 in allid and cid - 1 in allid and cid not in allid:
                return cid

print(solve(lines))
