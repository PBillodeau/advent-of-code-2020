import re

f = open("seven.txt", "r")
rules = f.read().replace("bags","").replace("bag", "").split('\n')

def get_container(rule):
    return re.search("\w+\s\w+", rule).group()

def get_contained(rule):
    return map(lambda x: x.strip(), rule.split("contain ", 1)[1][:-1].split(",")) 

def num_bags_holding(prevBags):
    nextBags = prevBags.copy()

    for rule in rules:
        for prevBag in prevBags:
            if prevBag in rule:
                if get_container(rule) not in nextBags:
                    nextBags.append(get_container(rule))

    if len(prevBags) != len(nextBags):
        return num_bags_holding(nextBags)

    return len(nextBags) - 1


def held_by(prevBags, count):
    nextBags = {}

    for rule in rules:
        for container in prevBags:
            if get_container(rule) == container:
                for bag in get_contained(rule):
                    if bag != 'no other':
                        bagType = "".join(bag[1:]).strip()
                        bagValue = int(bag[0]) * prevBags[container]

                        if bagType in nextBags.keys():
                            nextBags[bagType] += bagValue
                        else:
                            nextBags[bagType] = bagValue

                        count += bagValue

    if nextBags:      
        return held_by(nextBags, count)
    
    return count
        
print("Part a: ", num_bags_holding(['shiny gold']))
print("Part b: ", held_by({'shiny gold': 1}, 0))
