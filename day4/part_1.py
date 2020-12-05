import re

with open('input.txt', 'r') as f:
    data = f.read()

data = data.split('\n\n')

print("Number of passports:", len(data))

passports = [passport.replace('\n', ' ') for passport in data]

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']

def validate(passport, required, optional):
    kv_pairs = passport.split()
    keys = [pair.split(':')[0] for pair in kv_pairs]

    toboggan_fields = required

    for field in optional:
        if field in toboggan_fields:
            toboggan_fields.remove(field)

    for key in required:
        if key not in keys:
            return False
    
    is_toboggan = all(key in keys for key in toboggan_fields)
    is_valid = all(key in keys for key in required)

    return is_toboggan or is_valid

valid = []

for passport in passports:
    valid.append(validate(passport, required_fields, optional_fields))

print("Valid passports:", sum(valid))
