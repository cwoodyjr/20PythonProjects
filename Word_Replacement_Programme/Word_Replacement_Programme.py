# a programme to replace words within strings
mystring = 'this string will be changed'
print(mystring)
wordToBeReplaced = input('what word would you like to replace? ')
wordReplacedWith = input('what word would you like to replace it with? ')
# stringToSearch = input('Enter a string')
# # wordToReplace = input('What shall we replace? :')
# # replacedWith = input('what shall we use instead? :')

# # #print(stringToSearch.replace(wordToReplace,replacedWith))
# # stringToSearch = stringToSearch.replace(wordToReplace,replacedWith)
# # print(stringToSearch)

print(mystring.replace(wordToBeReplaced, wordReplacedWith))
