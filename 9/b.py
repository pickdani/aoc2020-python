lines = [int(x) for x in open('input').read().splitlines()]

def solve(lines):
    invalid = 50047984 # answer to previous question
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                seq = [lines[x] for x in range(i, j+1)]
                if sum(seq) == invalid:
                    return min(seq) + max(seq)


print(solve(lines))
