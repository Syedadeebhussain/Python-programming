#Problem Statement: Pangram Checker
#You are tasked with creating a Python function to determine whether a given string is a pangram. 
 #  A pangram is a sentence that contains every letter of the alphabet at least once.
#Write a Python function named "is_pangram" that takes a string as input and returns True if it is a pangram, and False otherwise.
 #Your function should be case-insensitive, meaning that it should consider both uppercase and lowercase letters when checking for the presence of each letter of the alphabet.
  # Example:
               # def is_pangram(sentence):
                    # Your implementation here

                # Test cases
                #print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
                #print(is_pangram("Hello, world!"))  # Output: False
                #print(is_pangram("Pack my box with five dozen liquor jugs"))  # Output: True
                #print(is_pangram("A quick brown fox"))  # Output: False
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str:
         return False
   return True
a='The five boxing wizards jump quickly.'
print(ispangram(a.lower()))