#  .strip(), len(), .lower(), .upper(), .split()

# strip basically removes leading and trailing white spaces
text = input('Input: ')
print(text)
print(text.strip())

#  length of the text value (int)
print(len(text))

#  lowecase all letters
print(text.lower())

#  uppercase all letters
print(text.upper())

#  split will divide the string into an array with any kind of delimiter which has been provided
another_text = "hello, srini, how, are, you, doing"
print(another_text.split(','))

#.find()  - linear search and give the index where its found for the first time
str = 'hello'
print(str.find('l')) 

# count of the char in the string
print(str.count('l'))

