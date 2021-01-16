xs = [int(x) for x in open('input').read().splitlines()]

def solve(xs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            for k in range(len(xs)):
                if i != j != k and xs[i] + xs[j] + xs[k] == 2020:
                    return xs[i] * xs[j] * xs[k]
print(solve(xs))
