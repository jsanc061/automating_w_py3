import re   # required to access regex library

# phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNum = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') 
# matchingRegexObject = phoneNum.search('My phone number is 121-151-4561.')
matchingRegexObject = phoneNum.search('My phone number is (121) 151-4561.')
print('Phone number found: ' + matchingRegexObject.group())

print(matchingRegexObject.groups())

areaCode, phone_num = matchingRegexObject.groups()
print('User area code: ' + areaCode + '\nUser phone number: ' + phone_num)

# matching multiple groups with the pipe '| '
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') 
mo = batRegex.search('Batmobile lost a wheel chasing a helicopter') 
print(mo.group())
print(mo.group(1))

# optional matching with the question mark '?'
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman and Batwoman')
print(mo1.group())

# matching one or more with the plus '+'
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

# Matching Specific Repetitions with Curly Brackets
big_laughs = re.compile(r'(Ha){3}')
big = big_laughs.search('I cant contain myself. Ha.. HaHaHa... HaHaHaHaHa')
print(big.group())

big_laughs = re.compile(r'(Ha){2,}')
big = big_laughs.search('I cant contain myself. Ha.. HaHaHa... HaHaHaHaHa')
print(big.group())

greedyBigLaughs = re.compile(r'(Ha){1,5}')  # matches the longest string possible
mo1 = greedyBigLaughs.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')    # matches the shortest string possible
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# The findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # has no groups
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)   # returns a list of string matches

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)   # returns a list of tuples of string matches
