lines = open('input').read().splitlines()

def findSwap(last):
    for i in range(last+1, len(lines)):
        line = lines[i]
        command = line.split()[0]
        if command == 'nop' or command == 'jmp':
            return i

def solve(lines):

    end = len(lines)
    lastswap = 0

    while True:
        currentSwap = findSwap(lastswap)
        lastswap = currentSwap

        ans = 0
        indicies = []
        index = 0

        while True:
            if index in indicies:
                break

            if index == end:
                return ans

            indicies.append(index)
            line = lines[index]
            command = line.split()[0]
            sign = line.split()[1][0]
            val = int(line.split()[1][1:])

            if sign == '+':
                sign = 1
            else:
                sign = -1

            if command == 'acc':
                ans += (sign * val)
                index += 1
            # execute the jump, either by default or from swapped nop
            elif (command == 'jmp' and index != currentSwap) or \
                (command == 'nop' and index == currentSwap):
                index += (sign * val)
            # execute nop, either by default or from swapped jmp
            elif (command == 'nop' and index != currentSwap) or \
                (command == 'jmp' and index == currentSwap):
                index += 1

print(solve(lines))
