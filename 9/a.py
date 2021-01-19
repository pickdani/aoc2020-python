lines = [int(x) for x in open('input').read().splitlines()]

def solve(lines):

    for current in range(25, len(lines)):
        prev = []
        # construct list of previous 25 numbers
        for j in range(current - 25, current):
            prev.append(lines[j])

        x = lines[current]

        valid = False
        # check if sum of previous equals current for valid
        for i in range(len(prev)):
            for k in range(len(prev)):
                if prev[i] + prev[k] == x:
                    valid = True
                    break
        if not valid:
            return x

print(solve(lines))
