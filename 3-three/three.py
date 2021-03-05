slope = []
f = open("three.txt", "r")
for line in f.readlines():
    slope.append(list(line))

print(slope)

def traverse(right, down):
    x = 0
    y = 0 
    trees = 0

    while y < len(slope) - 1:
        x = (x + right) % 31
        y += down
        
        if (slope[y][x] == '#'):
            trees += 1

    return trees

print("Part a: ", traverse(3, 1))
print("Part b: ", traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2))