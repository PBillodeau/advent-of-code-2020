import re

f = open("four.txt", "r")
passports = f.read().split('\n\n')

def fields_present(passport):
    byr = re.search("byr:", passport)
    iyr = re.search("iyr:", passport)
    eyr = re.search("eyr:", passport)
    hgt = re.search("hgt:", passport)
    hcl = re.search("hcl:", passport)
    ecl = re.search("ecl:", passport)
    pid = re.search("pid:", passport)
    
    return byr and iyr and eyr and hgt and hcl and ecl and pid

def fields_valid(passport):   
    try:
        byr = int(re.search("byr:\d{4}($| |\n)", passport).group().strip()[4:])
        iyr = int(re.search("iyr:\d{4}($| |\n)", passport).group().strip()[4:])
        eyr = int(re.search("eyr:\d{4}($| |\n)", passport).group().strip()[4:])
        hgt = re.search("hgt:\d*(cm|in)($| |\n)", passport).group().strip()[4:]
        hcl = re.search("hcl:\#([a-f0-9]{6})($| |\n)", passport).group()
        ecl = re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)($| |\n)", passport).group()
        pid = re.search("pid:(\d{9})($| |\n)", passport).group()
    except:
        return False

    if not (1920 <= byr and byr <= 2002):
        return False

    if not (2010 <= iyr and iyr <= 2020):
        return False

    if not (2020 <= eyr and eyr <= 2030):
        return False

    if hgt[-2:] == 'cm':
        if not (150 <= int(hgt[:-2]) and int(hgt[:-2]) <= 193):
            return False
    else:
        if not (59 <= int(hgt[:-2]) and int(hgt[:-2]) <= 76):
            return False

    return True

presentPassports = 0
validPassports = 0
for passport in passports:
    if fields_present(passport):
        presentPassports += 1
    if fields_valid(passport):
        validPassports += 1

print("Part a: ", presentPassports)
print("Part b: ", validPassports)