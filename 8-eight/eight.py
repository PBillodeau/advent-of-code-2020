f = open("eight.txt", "r")
commands = f.read().split('\n')

def execute(commands):
    addr = 0
    acc = 0
    prevAddr = []

    while addr not in prevAddr:
        prevAddr.append(addr)

        if addr == len(commands):
            break

        if commands[addr][:3] == 'nop':
            addr += 1
        elif commands[addr][:3] == 'acc':
            if commands[addr][4] == '+':
                acc += int(commands[addr][5:])
            else:
                acc -= int(commands[addr][5:])

            addr += 1
        elif commands[addr][:3] == 'jmp':
            if commands[addr][4] == '+':
                addr += int(commands[addr][5:])
            else:
                addr -= int(commands[addr][5:])

    return [acc, addr]

def fix(commands):
    addr = 0
    changeAddr = 0
    testCommands = commands.copy()
    
    while addr != len(commands):
        [acc, addr] = execute(testCommands)        
        testCommands = commands.copy()
        [testCommands, changeAddr] = flip_command(testCommands, changeAddr)
        changeAddr += 1

    return acc

def flip_command(testCommands, addr):

    if testCommands[addr][:3] == 'nop':
        testCommands[addr] = testCommands[addr].replace('nop', 'jmp')
    elif testCommands[addr][:3] == 'jmp':
        testCommands[addr] = testCommands[addr].replace('jmp', 'nop')
    else:
        addr += 1
        [testCommands, addr] = flip_command(testCommands, addr)

    return [testCommands, addr]

print("Part a: ", execute(commands)[0])
print("Part b: ", fix(commands))