import re

f = open("five.txt", "r")
boardingPasses = f.read().split('\n')

def get_id(boardingPass):
    boardingPass = re.sub('(B|R)', '1', boardingPass)
    boardingPass = re.sub('(F|L)', '0', boardingPass)

    return int(boardingPass, 2)

def find_missing(ids):   
    for id in range(ids[0], ids[-1]):
        if id not in ids:
            return id

    return -1

ids = list(map(get_id, boardingPasses))

ids.sort()

print("Part a: ", ids[-1])
print("Part b: ", find_missing(ids))
