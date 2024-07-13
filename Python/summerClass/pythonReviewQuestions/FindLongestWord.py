word1 = input("Enter a word: ")
word2 = input("Enter a word: ")
word3 = input("Enter a word: ")

# find the longest word
longest_word = max(word1, word2, word3, key=len)

print("The longest word is:", longest_word)
