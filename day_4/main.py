import re


class Passport():
    def __init__(self, byr="", iyr="", eyr="",
                 hgt="", hcl="", ecl="", pid="", cid=""):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def reqPresent(self):
        req = self.reqList()
        if len(req) == 7:
            return True

    def reqList(self):
        # Generate List of Required Fields, Removing ones that are Missing
        values = [self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl,
                  self.pid]

        return list(filter(len, values))

    def strictRules(self):
        valid = []
        # Birth Year between 1920 and 2002
        try:
            if int(self.byr) in range(1920, 2003):
                valid.append(self.byr)
        except Exception:
            pass
        # Issue Year between 2012 and 2020
        try:
            if int(self.iyr) in range(2010, 2021):
                valid.append(self.iyr)
        except Exception:
            pass
        # Expiration Year between 2020 and 2030
        try:
            if int(self.eyr) in range(2020, 2031):
                valid.append(self.eyr)
        except Exception:
            pass
        # Height between 150 and 193cm or 59 and 76in
        try:
            match = re.match(r'(\d+)(\w+)', self.hgt)
            if match:
                height = match.groups()
                if height[1].lower() == 'cm':
                    if int(height[0]) in range(150, 194):
                        valid.append(self.hgt)
                elif height[1].lower() == 'in':
                    if int(height[0]) in range(59, 77):
                        valid.append(self.hgt)
        except Exception:
            pass
        # Hair Color must be hex color code
        try:
            if re.match(r'#[a-f0-9]{6}', self.hcl):
                valid.append(self.hcl)
        except Exception as e:
            print(self.hcl)
            print(e)
        # Eye Color must be in list
        try:
            if self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid.append(self.ecl)
        except Exception as e:
            print(self.ecl)
            print(e)
        # Passport ID must be exactly 9 digits in length
        try:
            if re.match(r'[0-9]{9}', self.pid):
                if len(self.pid) == 9:
                    valid.append(self.pid)
        except Exception as e:
            print(self.pid)
            print(e)

        if len(valid) == 7:
            print(valid[6])
            return True
        else:
            return False


def validator(passport):
    # Validate passport return True if valid passport detected
    if passport.reqPresent():
        return True
    else:
        return False


def main():
    filename = 'input'

    passports = []
    with open(filename) as data:
        data = data.read()
        source = data.split('\n\n')
        for line in source:
            line = re.split(' |\n', line)
            passport = Passport()
            for d in line:
                try:
                    key, value = d.split(':')
                except Exception:
                    print(d)
                if key == "byr":
                    passport.byr = value
                elif key == "iyr":
                    passport.iyr = value
                elif key == "eyr":
                    passport.eyr = value
                elif key == "hgt":
                    passport.hgt = value
                elif key == "hcl":
                    passport.hcl = value
                elif key == "ecl":
                    passport.ecl = value
                elif key == "pid":
                    passport.pid = value
                elif key == "cid":
                    passport.cid = value

            passports.append(passport)

    valid = 0
    strict_valid = 0
    for passport in passports:
        if validator(passport):
            valid += 1
        if passport.strictRules():
            strict_valid += 1

    print(f'Relaxed Rule Valid: {valid}')
    print(f'Strict Rule Valid: {strict_valid}')


if __name__ == "__main__":
    main()
