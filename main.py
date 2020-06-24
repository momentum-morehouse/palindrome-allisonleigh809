# function which return reverse of a string 
import re 
# def onePalindrome(s): 
#     return s == s[::-1] 
# s = "malayalam"
# ans = onePalindrome(s) 
  
# if ans: 
#     print("Is a palindrome") 
# else: 
#     print("Is not a palindrome") 

# def twoPalindrome(s):
#   return s == s[::-1]
#   s = "stunt nuts"
#   ans = twoPalindrome(s)

# if ans:
#     print("Is a palindrome")
# else:
#     print("Is not a palindrome")

# def threePalindrome(s):
#   return s == s[::-1]
#   s = "borrow or rob?"
#   ans = threePalindrome(s)

# if ans: 
#   print("Is a palindrome")
# else:
#   print("Is not a palindrome")

# def nonPalindrome(s):
#   return s == s[::-1]
#   s = "stunt nuts"
#   ans = nonPalindrome(s)

# if ans: 
#   print("Is a palindrome")
# else:
#   print("Is not a palindrome")

# def nontwoPalindrome(s):
#   return s == s[::-1]
#   s = "rome"
#   ans = nontwoPalindrome(s)

# if ans: 
#   print("Is a palindrome")
# else:
#   print("Is not a palindrome")

# def nonthreePalindrome(s):
#   return s == s[::-1]
#   s = "rome"
#   ans = nonthreePalindrome(s)

# if ans: 
#   print("Is a palindrome")
# else:
#   print("Is not a palindrome")

#============================
def is_palindrome():
  name = input('Please enter your name?')
  print('Hello ' + name + '!')

def get_phrase():
  word = input('Enter a word or phrase to see if it is a palindrome: ')
  cleaned_phrase = re.sub(r'[^A-Za-z]', '', word.lower())

  if cleaned_phrase == cleaned_phrase[::-1]:
    print(word, 'IS a palindrome')
  else:
    print(word, 'IS NOT a palindrome')
  
  # get_tests():
  # get_name()
  # get_phrqse()
is_palindrome() 
get_phrase()
