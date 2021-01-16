lines = [x for x in open('input').read().splitlines()]

def solve(lines):
    ans = 0

    for line in lines:
        words = line.split()

        p1, p2 = [int(x) for x in words[0].split('-')]
        c = words[1][0]
        s = words[2]

        if (s[p1 - 1] == c) ^ (s[p2 - 1] == c):
            ans += 1

    return ans

print(solve(lines))
