lines = [x for x in open('input').read().splitlines()]

def solve(lines):
    ans = 0

    for line in lines:
        words = line.split()

        lo, hi = [int(x) for x in words[0].split('-')]
        c = words[1][0]
        s = words[2]

        count = 0
        for i in s:
            if i == c:
                count += 1

        if lo <= count <= hi:
            ans += 1

    return ans

print(solve(lines))
