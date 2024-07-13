# Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet 
# (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

def LetterChanges(str):
  result = ""
  vowels = ['a', 'e','i','o','u']
  
  for i in str:
    if i == 'z':
      newChar == 'a'
    elif i == 'Z':
      newChar == 'A'
    elif i.isalpha():
      newChar = chr(ord(i)+ 1)
    else:
      newChar = x
    if newChar in vowels:
      newChar = newChar.upper()
    result = result + newChar
  return result





print(LetterChanges("chiedozie"))