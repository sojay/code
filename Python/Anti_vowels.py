test_word = raw_input("Enter any word: ")
def anti_vowel(text):
  cons = ''
  for letter in text:
    if str(letter.lower()) not in "aeiouAEIOU":
      cons += letter
  return cons
print anti_vowel(test_word)