# Function to validate a phone number in python
import re      # re is a regular expression

def phoneNumberValidator(number):
    pattern = '(^[6-9][0-9]{9}$)|(^[0][6-9][0-9]{9}$)|[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern, str(number)):
        return True
    return False

def emailValidation(email):
    pattern = " ^[0-9a-z][a-z0-9_.]{4,13}[a-z0-9][@][0-9a-z]{3,18}[.][a-z]{2,4}$ "
    if re.match(pattern, email):
        return True
    return False

