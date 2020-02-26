# raw strings

print(r'new line 1 \n new line 2')
# output: new line 1 \n new line 2
# r prints line as it is

# printing emojis
# reference url: https://unicode.org/emoji/charts/full-emoji-list.html

print("\U0001F606 is a face")


#python as calculator using print function
print(2+3)
# output: 5

# operator for using calculation in python
# + = addition
# - = substraction
# * = multiplication
# / = division
# % = modulous or remainder
# **= exponent or power of

print(2+2)
print(3-2)
print(2*3)
print(9/3) #floating point division means it gives answer in decimals.
print(9//3) # integer division with no decimals.
print(4%3)
print(2**2)
print(4**0.5) #finding square roots in floating point
# round function
print(round(2**0.5,4)) #rounds square of 2 to 4 digits

# output
# 4
# 1
# 6
# 3.0 
# 3
# 1
# 4
# 2
#1.4142


# multiple operater statement calculation orders
print(2**2/2*6-4*(3-4/2))
# output: 8.0 
# precedence rule and associative rule 
# precedence rule 
# highest to lowest
# parenthesis- 1
# exponent - 2 associative right to left direction
# *,/,//,% -3 associative left to right direction
# +,- = associative left to right direction
