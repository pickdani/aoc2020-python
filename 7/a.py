lines = [x.strip() for x in open('input').read().splitlines()]

''' map color to mapping of color to num of bags contained
   {
    'darkolive' : {'fadedblue' : 1, 'brightwhite' : 3}
    'darkolive' : {'fadedblue' : 1, 'brightwhite' : 3}
    ...
    }
'''

bags = {}

def initBags(lines):
    # init bags dict
    for line in lines:
        words = line.split('bags')[0].split()
        color = words[0] + words[1]

        rest = line.split('contain')[1].split(',')

        inner = {}

        # inner dict is empty if no inner bags
        if 'no other bags' not in rest[0]:
            for bag in rest:
                contains = bag.strip().split()
                value = contains[0]
                col = contains[1] + contains[2]
                inner[col] = value

        bags[color] = inner

# given a starting bag goes until empty or found gold
# return true if shinygold reached, otherwise false
def containsGold(bag):
    # base case 1
    if 'shinygold' in bag.keys():
        return True

    # base case 2
    if not bag:
        return False

    # otherwise call containsGold on all inner bags
    # if any inner bags contain shiny gold return true
    for inner in bag.keys():
        if containsGold(bags[inner]):
            return True


def solve(lines):
    initBags(lines)

    ans = 0
    # look at each bag
    for k,v in bags.items():
        if containsGold(bags[k]):
            ans += 1

    return ans

print(solve(lines))
