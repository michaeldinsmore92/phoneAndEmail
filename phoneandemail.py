#! /usr/bin/env python3


import re, pyperclip


# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)    # first separator
\d\d\d    # first three digits
-    # separator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x)    # extension word (optional)
(\d{2,5}))?   # extension number (optional)
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@somet.+_thing.com

[a-zA-Z0-9_.+]+    # name
@    # @ symbol
[a-zA-Z0-9_.+]+    # domain name
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

# TODO: Extract email/phone numbers from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# TODO: Copy the extracted email/phone numbers to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)