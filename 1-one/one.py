nums = []
f = open("one.txt", "r")
for line in f.readlines():
    nums.append(int(line))

# For a + b = 2020, one must be greater than 1010, and one must be less than 1010. There are very few values in the array less than 1010, so we can speed things up quite a bit
a = []
b = []
for num in nums:
    if num < 1010:
        a.append(num)
    else:
        b.append(num)

try:
    for aValue in a:
        for bValue in b:
            if aValue + bValue == 2020:
                print("Part a:", (aValue * bValue))
                raise StopIteration
except StopIteration: pass

# For a + b + c = 2020, at least one must be greater than 674, so we can speed things up... a little better than trying _every_ combo :)
a = []
b = []
for num in nums:
    if num < 674:
        a.append(num)
    else:
        b.append(num)

try:
    for aValue in a:
        for bValue in b:
            for aValue2 in a:
                if aValue + bValue + aValue2 == 2020:
                    print("Part b:", aValue * bValue * aValue2)
                    raise StopIteration
except StopIteration: pass
