lines = [x.strip() for x in open('input').read().splitlines()]

def solve(lines):
    ans = 0
    answers = set()
    for line in lines:
        if not line:
            ans += len(answers)
            answers = set()
        else:
            for c in line:
                answers.add(c)
    return ans

print(solve(lines))
