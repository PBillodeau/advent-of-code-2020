f = open("six.txt", "r")
answers = f.read().split('\n\n')

anyoneYes = 0
everyoneYes = 0
for answer in answers:
    
    people = len(answer.split('\n'))
    totals = {}

    for letter in answer:
        if letter not in totals:
            totals[letter] = 1
        else:
            totals[letter] += 1

    if people in totals.values():
        for value in totals.values():
            if people == value:
                everyoneYes += 1
    
    anyoneYes += len(list(set(answer.replace('\n', ''))))

print("Part a: ", anyoneYes)
print("Part b: ", everyoneYes)
