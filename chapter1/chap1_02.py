# Chapter 1 lesson 2

#escape sequences help to use unusable characters inside a string usable in a string
#example 
#print("this is "double quotes" inside double quotes")
#output: error! #double quotes cannot be used inside double quotes! 
#escape sequences allow to use double quotes inside double quotes

print("this book called \"strings\" is boring!")
# output: this book called "strings" is boring! 
#\ backslash is used for escaping sequences 
print('I\'m bored of using \'escape sequence\' again!')
# output: I'm bored of using 'escape sequence' again!
# different escape sequences
# \'    single quote
# \"    double quote
# \\    backslash
# \n    new line
# \t    tab
# \b    backspace

print('I\'m bored!')
print("your \"Iphone\" is old")
print("this is line A\nthis is line B")
print("\tPlease write article in this way")
print("Here you originally   have a space\nHere you originally  \bhad a space")
print("linux and macos uses \\ backslash for terminal but windows is uses / which is confusing!")
# Output
# I'm bored!
# your "Iphone" is old
# this is line A
# this is line B
#         Please write article in this way
# Here you originally   have a space
# Here you originally had a space
# linux and macos uses \ backslash for terminal but windows is uses / which is confusing!


# comments are used anything after # character!
# comments are ignored by python interpreter and are mostly used to comment codes for readers to understand codes
# this is a comment