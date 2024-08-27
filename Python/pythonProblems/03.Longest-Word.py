# Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty.


def LongestWord(sen):
  longest = ""
  longestCount = 0 
  
  for x in sen.split(): #< ---- splits the sentence into substrings
    tempCount = 0 
    for y in x: # <- counts the letters in every sub string
      if y.isalpha(): #<---- if its a letter not a number than add the count to the tempCount variable
        tempCount += 1
    if tempCount > longestCount:
      longestCount = tempCount
      longest = x
      
  return longest













print(LongestWord("Hello there my name is chiedozie ehileme"))