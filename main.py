# function which return reverse of a string 
  
def onePalindrome(s): 
    return s == s[::-1] 
s = "malayalam"
ans = onePalindrome(s) 
  
if ans: 
    print("Is a palindrome") 
else: 
    print("Is not a palindrome") 

def twoPalindrome(s):
  return s == s[::-1]
  s = "stunt nuts"
  ans = twoPalindrome(s)

if ans:
    print("Is a palindrome")
else:
    print("Is not a palindrome")

def threePalindrome(s):
  return s == s[::-1]
  s = "borrow or rob?"
  ans = threePalindrome(s)

if ans: 
  print("Is a palindrome")
else:
  print("Is not a palindrome")

def nonPalindrome(s):
  return s == s[::-1]
  s = "stunt nuts"
  ans = nonPalindrome(s)

if ans: 
  print("Is a palindrome")
else:
  print("Is not a palindrome")

def nontwoPalindrome(s):
  return s == s[::-1]
  s = "rome"
  ans = nontwoPalindrome(s)

if ans: 
  print("Is a palindrome")
else:
  print("Is not a palindrome")

def nonthreePalindrome(s):
  return s == s[::-1]
  s = "rome"
  ans = nonthreePalindrome(s)

if ans: 
  print("Is a palindrome")
else:
  print("Is not a palindrome")