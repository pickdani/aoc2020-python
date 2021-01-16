lines = [x.strip() for x in open('input').read().splitlines()]


def solve(lines):

    ans = 0 # num valid passports

    passport = {} # current passport
    for line in lines:
        if not line: # end of passpost
            valid = True
            # check validty of passport

            fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            # invalid if any fields are missing
            for field in fields:
                if field not in passport:
                    valid = False

            if valid:
                ans += 1

            passport = {} # clear passport
        else:
            fields = line.split()
            for field in fields:
                key, val = field.split(':')
                passport[key] = val

    return ans

print(solve(lines))
