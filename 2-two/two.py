f = open("two.txt", "r")
values = f.read().split('\n')

def parse(input):
    [first, rest] = input.split('-', 1)
    [second, rest] = rest.split(' ', 1)
    [letter, password] = rest.split(':', 1)

    return [int(first), int(second), letter, password.strip()]

def is_valid_a(min, max, letter, password):
    count = password.count(letter)

    return min <= count and count <= max

def is_valid_b(first, second, letter, password):
    if (len(password) < first):
        return False
    
    if len(password) < second:
        return password[first - 1] == letter

    return (password[first - 1] == letter or password[second - 1] == letter) and password[first - 1] != password[second - 1]

validCountA = 0
validCountB = 0
for value in values:
    [first, second, letter, password] = parse(value)

    if is_valid_a(first, second, letter, password):
        validCountA += 1
    if is_valid_b(first, second, letter, password):
        validCountB += 1

print("Part a:", validCountA)
print("Part b:", validCountB)
