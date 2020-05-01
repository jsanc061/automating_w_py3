import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

# user_num = input("Enter your phone number: ")

# while isPhoneNumber(user_num) != True:
#     if isPhoneNumber(user_num) == True:
#         print("Valid phone number")
#     else:
#         user_num = input("Please enter a valid phone number: ")
        
message = 'Call me tomorrow at 555-151-1515. My office phone is 210-151-4884.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

# matching with regex

# phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNum = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') 
# matchingRegexObject = phoneNum.search('My phone number is 121-151-4561.')
matchingRegexObject = phoneNum.search('My phone number is (121) 151-4561.')
print('Phone number found: ' + matchingRegexObject.group())

print(matchingRegexObject.groups())

areaCode, phone_num = matchingRegexObject.groups()
print('User area code: ' + areaCode + '\nUser phone number: ' + phone_num)

# matching multiple groups with the pipe | 
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') 
mo = batRegex.search('Batmobile lost a wheel chasing a helicopter') 
print(mo.group())
print(mo.group(1))