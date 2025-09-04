# Finding Text patterns with Regular Expressions
# regualr expressions are a powerful way to search and manipulate strings
# They are also called regex or regexp

import re

string = "My number is 415-555-4242. Call me tomorrow, or at 415-555-9999."

pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # pattern to match phone numbers

# matches = pattern.search(string)
# print(matches.group())

matches = pattern.findall(string) # findall() returns a list of all matches in the string
print(matches)

# Grouping with Parentheses
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search(string)
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

area_code, main_number = mo.groups()
print("Area code:", area_code , "and Main number:", main_number)

# Using Escape characters
phone_re = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
string = "My number is (415) 555-4242."
mo = phone_re.search(string)
print(mo.group())

# The pipe | character is called a "pipe" and is used to match one of many possible patterns
bat_re = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_re.search("Batmobile lost a wheel")  
print(mo.group())
print(mo.group(1))

# Using character classes and negative character classes
vowel_re = re.compile(r'[aeiouAEIOU]')
consonant_re = re.compile(r'[^aeiouAEIOU .,]') # ^ inside [] means negation
print(vowel_re.findall("RoboCop eats baby food."))
print(consonant_re.findall("RoboCop eats baby food."))

# Using shorthand character classes
# \d - any digit, \D - any non-digit
# \w - any alphanumeric character, \W - any non-alphanumeric character
# \s - any whitespace character, \S - any non-whitespace character

xmas_re = re.compile(r'\d+\s\w+')
print(xmas_re.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"))

# Matching everything with dot character
at_re = re.compile(r'.at')
print(at_re.findall("The cat in the hat sat on the flat mat."))

# Matching everything with dot-star
name_re = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_re.search("First Name: Al Last Name: Sweigart")
print(mo.group(1))
print(mo.group(2))

# Greedy and non-greedy matching
greedy_pattern = re.compile(r'(Ha){3,5}')
mo = greedy_pattern.search("HaHaHaHaHa")
print(mo.group())

nongreedy_pattern = re.compile(r'(Ha){3,5}?')
mo = nongreedy_pattern.search("HaHaHaHaHa")
print(mo.group())

# Matching newlines with the dot character
no_newline_pattern = re.compile('.*')
newline_pattern = re.compile('.*', re.DOTALL) # re.DOTALL makes dot match newlines  
string = """Serve the public trust.
Protect the innocent.   
Uphold the law."""
print(no_newline_pattern.search(string).group())
print()
print(newline_pattern.search(string).group())

# Matching start and end of string
begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search("Hello world!"))

ends_with_number = re.compile(r'\d$')
print(ends_with_number.search("Your number is 42"))

whole_string_is_number = re.compile(r'^\d+$')
print(whole_string_is_number.search("1234567890"))

pattern = re.compile(r'\bcat\b') # \b is a word boundary
print(pattern.search("The cat in the hat."))

pattern = re.compile(r'\Bcat\B') # \B is a non-word boundary
print(pattern.search("The cat in the hat."))

# case-insensitive matching
robocop = re.compile(r'robocop', re.I) # re.I makes the pattern case-insensitive
print(robocop.search("RoboCop is part of a crime-fighting duo."))
print(robocop.search("ROBOCOP protects the innocent."))

# substituting strings with the sub() method
names_regex = re.compile(r'Agent \w+')
print(names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# Managing complex regexes with the VERBOSE flag
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
    )''', re.VERBOSE)
mo = phone_regex.search("My number is (415) 555-4242 ext. 12345.")
print(mo.group())

num_re = re.compile(r'\d+')
print(num_re.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))