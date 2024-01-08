#Problem Statement: Fibonacci Series Analysis
# You are tasked with analyzing the Fibonacci series up to a specified number of terms. 
 # The goal is to determine and display information about each term in the series based on the following criteria:
 #          If the term is even, display: "It's even."
  #              If the term is odd, display: "It's odd."
   #             If the term is both odd and prime, display: "It's both odd and prime."
#Write a Python program that takes input for the number of terms in the Fibonacci series and outputs the analyzed information for each term in a readable format. 
  #The program should include a function to determine whether a given number is prime.
 # Consider the first two terms in the Fibonacci series as 0 and 1. 
# Use a loop to generate the remaining terms and analyze each one based on the specified criteria.

    #            PERFORM IT BY USING A FUNCTION.
                
               # Example - 
                #Enter the number of terms in the Fibonacci series: 8
                
                #Fibonacci series with 8 terms:
                #0 - It's even.
                #1 - It's odd.
                #1 - It's odd.
                #2 - It's even.
                #3 - It's odd and prime.
                #5 - It's odd and prime.
                #8 - It's even.
                #13 - It's odd and prime.
def isprime(c):
    d=0
    for i in range(1,c+1):
        if c%i==0:
            d+=1
    if d==2:
        return True
    else:
        return False
def fibonacci(n):
    a=0
    b=1
    for i in range(2,n):
        c =a+b
        a=b
        b=c
        if c%2!=0 and isprime(c):
           print(f"{c}-It's odd and prime.")
        elif c%2==0:
            print(f"{c}-It's even.")
        elif c%2!=0:
            print(f"{c}-It's odd.")
n=int(input("Enter the number of terms in the Fibonacci series: "))
a=0
b=1
print(f"{a} - It's even.")
print(f"{b} - It's odd.")
fibonacci(n)
