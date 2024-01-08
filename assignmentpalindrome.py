#Problem Statement: Palindrome Operations
# Write a Python program that performs specific operations on palindrome numbers within a given range. 
# The program should follow these rules:
# Define a function square_root to calculate the square root of a number.
# Define a function power to calculate the power of a number.
# Define a function is_palindrome to check if a number is a palindrome.
# Take user input for the starting and ending range (inclusive).
#Display the operations on palindrome numbers within the specified range:
#If the palindrome number is even, perform the square root operation on it.
#If the palindrome number is odd, perform the power operation on it.

#Example:
#Enter the starting range: 100
#Enter the ending range: 250
#Operations on palindrome numbers within the range 100 to 250:

                 #   101 - Power of 2: 10201
                  #  111 - Power of 2: 12321
                   # 121 - Power of 2: 14641
                    #131 - Power of 2: 17161
                 #   141 - Power of 2: 19881
                  #  151 - Power of 2: 22801
                  #  161 - Power of 2: 25921
                  #  171 - Power of 2: 29241
                  #  181 - Power of 2: 32761
                  #  191 - Power of 2: 36481
                  #  202 - Square Root: 14.212670
                  #  212 - Square Root: 14.560219
                  #  222 - Square Root: 14.899664
                  #  232 - Square Root: 15.231546
                   # 242 - Square Root: 15.556349
def square_root(z):
    print(f"{z}->{(z**0.5):.6f}")
def power(z):
    print(f"{z}->{(z**2)}")
def is_palindrome(a,b):
        for i in range(a,b+1):
            c=str(i)
            rev=c[::-1]
            if rev==c:
              c=eval(c)
              if(c%2==0):
                square_root(c)
              else:
                power(c)  
a=int(input("Enter the starting range: "))
b=int(input("Enter the ending range: "))
print(f"Operations on palindrome numbers within the range {a} to {b}:")
is_palindrome(a,b)