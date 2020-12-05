import re

with open('input.txt', 'r') as f:
    data = f.read()

data = data.split('\n\n')

print("Number of passports:", len(data))

passports = [passport.replace('\n', ' ') for passport in data]

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']

valid_hcl = re.compile(r'^#[0-9a-f]{6}$')
valid_hgt = re.compile(r'((1[5-8][0-9]|19[0-3])cm|(^[5-6][0-9]|^7[0-6])in)')
valid_eyr = re.compile(r'^\d{4}$')
valid_pid = re.compile(r'^\d{9}$')

def validation_rules(passport, key):
    value = passport[key]

    if key == 'byr':
        return re.match(valid_eyr, value) and 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return re.match(valid_eyr, value) and 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return re.match(valid_eyr, value) and 2020 <= int(value) <= 2030
    elif key == 'hcl':
        return re.match(valid_hcl, value)
    elif key =='hgt':
        return re.match(valid_hgt, value)
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return re.match(valid_pid, value)
    elif key == 'cid':
        return True
    else:
        return False

def validate(passport, required, optional):
    kv_pairs = passport.split()

    pp = {}

    for pair in kv_pairs:
        k, v = pair.split(':')
        pp[k] = v

    keys = pp.keys()
    
    toboggan_fields = required

    for field in optional:
        if field in toboggan_fields:
            toboggan_fields.remove(field)
    
    is_toboggan = all(
        ([key in keys for key in toboggan_fields]) +
        ([validation_rules(pp, key) for key in keys])
    )

    is_valid = all(
        ([key in keys for key in required]) +
        ([validation_rules(pp, key) for key in keys])
    )

    print(is_valid, is_toboggan)

    return is_valid or is_toboggan

valid = []

for passport in passports:
    valid.append(validate(passport, required_fields, optional_fields))

print("Valid passports:", sum(valid))
