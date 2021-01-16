lines = open('input').read().splitlines()

def solve(lines):
    ans = 0
    indicies = []
    index = 0

    while True:
        if index in indicies:
            break

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
        elif command == 'jmp':
            index += (sign * val)
        elif command == 'nop':
            index += 1

    return ans

print(solve(lines))
