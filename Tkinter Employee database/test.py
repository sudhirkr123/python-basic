import re
def isvalid(num):
    pattern=re.compile('(0|91)?[-\s]?[6-9]\d{9}')
    return pattern.match(num)


num=input('enter the number:')
if isvalid(num):
    if len(num)==10:
        print("valid mobile number")
    else:
        print('invalid mobile number')
else:
    print('Invalid mobile number')

