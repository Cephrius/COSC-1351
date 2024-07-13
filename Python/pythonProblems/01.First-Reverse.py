# Question: Have the function FirstReverse(str_) take the str parameter
# being passed and return the string in reversed order.

def FirstReverse(str):
  result = ""
  rev = reversed(list(str))
  for letter in rev:
    result = result + letter
  return result 


print(FirstReverse("helloworld"))



