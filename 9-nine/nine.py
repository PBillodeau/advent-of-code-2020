f = open("nine.txt", "r")
preamable = 25
numbers = []
for line in f.readlines():
    numbers.append(int(line))

def is_valid(value, prevNums):
    valid = False

    for prevNum in prevNums:
        if value - prevNum in prevNums:
            valid = True
            break

    return valid

def find_rule_breaker(numbers, preamble):
    n = preamble

    while n < len(numbers):
        value = numbers[n]
        prevNums = numbers[n-preamble:n]

        if is_valid(value, prevNums):
            n += 1
        else:
            break

    return numbers[n]

def find_contiguous(value, numbers):
    start = 0
    end = 1

    while start < len(numbers):
        total = sum(numbers[start:end])
        
        if total == value:
            return min(numbers[start:end]) + max(numbers[start:end])
        if total < value:
            end += 1
        if total > value:
            start += 1
            end = start + 1
    
    return -1

print('Part a: ', find_rule_breaker(numbers, preamable))
print('Part b: ', find_contiguous(find_rule_breaker(numbers, preamable), numbers))