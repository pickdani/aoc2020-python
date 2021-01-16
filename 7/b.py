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

# given a bag returns how many bags are contained within it
def countInnerBags(bag):
    # base case, 'contains no other bags'
    if not bag:
        return 1
    # count bags on all inner bags and add them, plus 1 for current bag
    return 1 + sum([int(c) * countInnerBags(bags[n]) for n,c in bag.items()])

def solve(lines):
    initBags(lines)
    # count bags inside shiny gold, - 1 to exclude shiny gold itself
    return countInnerBags(bags['shinygold']) - 1

print(solve(lines))
