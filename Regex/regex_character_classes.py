import re   # IMPORTANT - required to use regex library

# Regex shorthand codes for common character classes
#
# \d    Any numeric digit from 0 to 9.
# \D    Any character that is not a numeric digit from 0 to 9.
# \w    Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W    Any character that is not a letter, numeric digit, or the underscore character.
# \s    Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S    Any character that is not a space, tab, or newline.
#

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, '+ 
                       '7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

# Creating Custom Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')    # character class for vowels
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# Negating a Character Class using the carot '^'
consonantRegex = re.compile(r'[^aeiouAEIOU]')   # character class for consonants
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# Matching a string that starts at the beginning of the searched text
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo)

mo2 = beginsWithHello.search('He said hello.')
print(mo2)

# Matching a string that ends with a numeric char from 0 to 9
endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print(mo)

mo = endsWithNumber.search('Your number is forty two.')
print(mo)

# Matching a string that begins and ends with one or more numeric characters
wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print(mo)

mo = wholeStringIsNum.search('12345xyz67890')
print(mo)

mo = wholeStringIsNum.search('12 34567890')
print(mo)

# The Wildcard character '.'
atRegex = re.compile(r'.at')    # matches for any character except for newline
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# Matching everything with Dot-Star '.*'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# Matching Newline with the Dot '.'
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)

newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)