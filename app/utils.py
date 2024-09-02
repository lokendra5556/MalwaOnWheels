import re
from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def validateName(name):
    pattern = "[a-zA-Z]+"
    if re.match(pattern, name):
        return True
    else:
        return False

def validatePhone(phone):
    pattern = "^(?=(?:[6-9]){1})(?=[0-9]{10}).*"
    if re.match(pattern, phone):
        return True
    else:
        return False
    
def validateCarRegNum(regNum):
    pattern = "^[A-Z]{2}[ -]?[0-9]{2}[ -]?[A-Z]{1,2}[ -]?[0-9]{4}$"
    if re.match(pattern, regNum):
        return True
    else:
        return False
    
def validateEmail(email):
    pattern = "^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
    if re.match(pattern, email):
        return True
    else:
        return False
    
def validateLicenceNum(licenceNum):
    pattern = "^[A-Z]{2}[0-9]{13}"

    if re.match(pattern ,licenceNum):
        return True
    else:
        return False

def hash(password):
    return pwd_context.hash(password)