lines = [x.strip() for x in open('input').read().splitlines()]


def solve(lines):

    ans = 0 # num valid passports

    passport = {} # current passport
    for line in lines:
        if not line: # end of passpost
            valid = True
            # check validty of passport

            if 'byr' in passport:
                birth = int(passport['byr'])
                if not (1920 <= birth <= 2002):
                    valid = False
            else:
                valid = False

            if 'iyr' in passport:
                year = int(passport['iyr'])
                if not (2010 <= year <= 2020):
                    valid = False
            else:
                valid = False

            if 'eyr' in passport:
                exp = int(passport['eyr'])
                if not (2020 <= exp <= 2030):
                    valid = False
            else:
                valid = False

            if 'hgt' in passport:
                height = passport['hgt']
                if height.endswith('cm'):
                    hval = int(height[:len(height) - 2])
                    if not (150 <= hval <= 193):
                        valid = False
                elif height.endswith('in'):
                    hval = int(height[:len(height) - 2])
                    if not (59 <= hval <= 76):
                        valid = False
                else:
                    valid = False
            else:
                valid = False

            if 'hcl' in passport and len(passport['hcl']) == 7:
                if not passport['hcl'].startswith('#'):
                    valid = False
                else:
                    rest = passport['hcl'][1:]
                    val = '1234567890abcdef'
                    for char in rest:
                        if char not in val:
                            valid = False
            else:
                valid = False

            if 'ecl' in passport:
                eye = passport['ecl']
                cols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if eye not in cols:
                    valid = False
            else:
                valid = False

            if 'pid' in passport:
                if len(passport['pid']) != 9:
                    valid = False
                digits = '1234567890'
                for x in passport['pid']:
                    if x not in digits:
                        valid = False
            else:
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
