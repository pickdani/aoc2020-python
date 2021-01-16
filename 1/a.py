xs = [int(x) for x in open('input').read().splitlines()]

def solve(xs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i != j and xs[i] + xs[j] == 2020:
                return xs[i] * xs[j]
print(solve(xs))
