lines = [x.strip() for x in open('input').read().splitlines()]

def solve(lines):
    ans = 0
    answers = []
    valid = set()
    people = 0
    for line in lines:
        if not line:
            for field in valid:
                if answers.count(field) == people:
                    ans += 1

            valid = set()
            answers = []
            people = 0
        else:
            people += 1
            for c in line:
                answers.append(c)
                valid.add(c)
    return ans

print(solve(lines))
